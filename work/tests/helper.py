from django.core.files.uploadedfile import InMemoryUploadedFile

from work.models import Project

from PIL import Image
from io import BytesIO


def create_project():
    """
    Returns a newly created Project object that has already been saved in the db.
    """
    return Project.objects.create(name='Test', url_slug='test', description='test',
            link='http://www.test.com', repository='http://www.test.com',
            one_line="Test project for tests.", best=False,
            languages='JavaScript,C', stack='React,Node', hosting='Heroku',
            current=False, public=False, extra_tags='API,Dataframes'
            )

def create_dummy_image(name):
    """
    Returns a newly created png format image file.
    """
    # New PIL Image
    image = Image.new(mode='RGB', size=(200,200))

    # BytesIO obj for saving the image
    image_io = BytesIO()

    # Save the image
    image.save(image_io, 'PNG')

    # Seek to start
    image_io.seek(0)

    return InMemoryUploadedFile(
        image_io, None, name, 'image/png', len(image_io.getvalue()), None
    )
    