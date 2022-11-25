from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry, ImageUrlCreateBatch

import pandas as pd
import math

def upload_tags(tags, custom_vision_project, training_client):
    for tag in tags:
        print(f'Create tag: {tag}')
        training_client.create_tag(custom_vision_project.id, tag)
    return

def Upload_Images_to_Azure(albums, custom_vision_project, training_client):
    tags = training_client.get_tags(custom_vision_project.id)

    image_count = len(albums)
    image_count_per_batch = 64
    batch_count = math.ceil(image_count / image_count_per_batch)
    
    print(f'albums_df_filename size {image_count}')

    for batch_iter in range(batch_count):
        print(f'Batch n°{batch_iter} creation...')
        print(f'Batch add image from index {image_count_per_batch * batch_iter} to {image_count_per_batch * batch_iter + image_count_per_batch}')

        image_list = []

        for index, row in albums[image_count_per_batch * batch_iter:image_count_per_batch * batch_iter + image_count_per_batch].iterrows():
            tag = next(t for t in tags if t.name == row["tags"])
            image_list.append(ImageUrlCreateEntry(url=row['cover_url'], tag_ids=[tag.id]))

            print(f'Batch add image: [index: {index}, tag: {tag.name}]')

        print(f'Batch size {len(image_list)}')

        upload_result = training_client.create_images_from_urls(custom_vision_project.id, ImageUrlCreateBatch(images=image_list))
        if not upload_result.is_batch_successful:
            print(f'Batch n° {batch_iter} succesfully uploaded')