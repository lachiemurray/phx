from factory import RelatedFactory, Sequence
from factory.django import ImageField
from factory.fuzzy import FuzzyText, FuzzyChoice
from factory_djoy import CleanModelFactory

from components.models import ALIGNMENT_CHOICES, BACKGROUND_CHOICES
from ..models import (
    News,
    Thumbnail,
    Component,
    Editorial,
    Embed,
    Feature,
    Image,
    ListItem,
    ListItems,
    Profile,
    ProfileMember,
    Quote,
    Table,
)


class ThumbnailFactory(CleanModelFactory):
    image = ImageField()

    class Meta:
        model = Thumbnail


class NewsFactory(CleanModelFactory):
    title = FuzzyText()
    summary = FuzzyText()

    RelatedFactory(ThumbnailFactory, 'news')

    class Meta:
        model = News


class ComponentFactory(CleanModelFactory):
    order = Sequence(lambda n: n)

    class Meta:
        model = Component


class EditorialFactory(CleanModelFactory):
    title = FuzzyText()
    content = FuzzyText()

    class Meta:
        model = Editorial


class EmbedFactory(CleanModelFactory):
    title = FuzzyText()
    content = FuzzyText()

    class Meta:
        model = Embed


class FeatureFactory(CleanModelFactory):
    title = FuzzyText()
    content = FuzzyText()
    align = FuzzyChoice([i[0] for i in ALIGNMENT_CHOICES])
    background = FuzzyChoice([i[0] for i in BACKGROUND_CHOICES])
    image = ImageField()

    class Meta:
        model = Feature


class ImageFactory(CleanModelFactory):
    caption = FuzzyText()
    image = ImageField()

    class Meta:
        model = Image


class ListItemsFactory(CleanModelFactory):
    class Meta:
        model = ListItems


class ListItemFactory(CleanModelFactory):
    title = FuzzyText()
    image = ImageField()

    class Meta:
        model = ListItem


class ProfileFactory(CleanModelFactory):
    title = FuzzyText()

    class Meta:
        model = Profile


class ProfileMemberFactory(CleanModelFactory):
    name = FuzzyText()
    role = FuzzyText()
    image = ImageField()

    class Meta:
        model = ProfileMember


class QuoteFactory(CleanModelFactory):
    quote = FuzzyText()
    author = FuzzyText()
    align = FuzzyChoice([i[0] for i in ALIGNMENT_CHOICES])
    background = FuzzyChoice([i[0] for i in BACKGROUND_CHOICES])
    image = ImageField()

    class Meta:
        model = Quote


class TableFactory(CleanModelFactory):
    title = FuzzyText()
    content = FuzzyText()

    class Meta:
        model = Table
