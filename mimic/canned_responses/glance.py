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

def get_image_by_key(image_key):
    """
    Get image by its image_id or name
    Assumes the name of one image is not the id of a different image
    Will work if the image_id and image_name are identical
    Assumes image_ids are unique but not names
    """
    image_dict = get_images()
    output_dict = {"images" : []}
    for image in image_dict['images']:
        if image['id'] == image_key:
            response = 200
            return (response, image)
            
        elif image['name'] == image_key:
           
            output_dict['images'].append(image)

    if len(output_dict['images']) > 0:
        #output dict is not empty return the dict
        response=200
        return (response, output_dict)

    # image key not in images return 404 not found
    response = 404
    return(response, '')

