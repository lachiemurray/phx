from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.utils import timezone
from .models import Topic

custom_topics = [
    ('general', 'General Enquiry'),
    ('misc', 'Miscellaneous / Other')
]


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'Form-input--text'}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'Form-input--text'}),
    )
    topic = forms.ChoiceField(
        required=True,
        choices=[],
        widget=forms.Select(attrs={'class': 'Form-select'}),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'Form-textarea'}),
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        choices = [(topic.pk, topic.topic) for topic in Topic.objects.all()]
        choices = [
            custom_topics[0]
        ] + choices + [
            custom_topics[1]
        ]
        self.fields['topic'].choices = choices

    def send_email(self):
        # get posted topic id
        # create list of custom topic keys
        # ascertain whether selected topic is from db or custom list
        topic = self.cleaned_data['topic']
        contactless_topics = [
            custom_topic[0] for custom_topic in custom_topics
        ]
        topic = None if topic in contactless_topics else topic

        # if posted topic id is from db rather than custom list,
        # retrieve its corresponding 'topic' field from its model
        # also extract which additional contacts to send email to
        if topic:
            topic_model = Topic.objects.get(pk=topic)
            topic_label = topic_model.topic
            contacts = topic_model.contact.values_list('email', flat=True)
            additional_recipients = list(contacts)
        else:
            topic_label = 'General/Misc'
            additional_recipients = []

        subject = 'Website message received'
        email = 'brightonphoenix@gmail.com'
        recipients = ['thegingerbloke@gmail.com'] + additional_recipients
        message = (
            'Website message received on {0}\n\n'
            'From: {1}\n'
            'Email: {2}\n'
            'Topic: {3}\n\n'
            'Message: {4}\n\n'
            '-----------------------------------\n\n'
        ).format(
            timezone.now(),
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            topic_label,
            self.cleaned_data['message'],
        )

        try:
            send_mail(subject, message, email, recipients)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
