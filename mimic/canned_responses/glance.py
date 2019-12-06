"""
Cannned responses for glance images
"""

from __future__ import absolute_import, division, unicode_literals

from mimic.canned_responses.json.glance.glance_images_json import (images,
                                                                   image_schema)
import json

def get_images():
    """
    Canned response for glance images list call
    """
    return images

def get_v2_images():
    """
    Canned response for glance images list call
    """
    return images


def get_image_schema():
    """
    Canned response for GET glance image schema API call
    """
    return image_schema

def get_image_by_id(image_id):
    """
    Get image by its image_id
    """
    image_dict = get_images()
    for image in image_dict['images']:
        if image['id'] == image_id:
            response = 200
            return (response, image)

    # image id not in images return 404 not found
    response = 404
    return(response, '')

