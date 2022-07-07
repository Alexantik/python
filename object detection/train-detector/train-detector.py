from logging import exception
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models  import ImageFileCreateBatch, ImageFileCreateEntry
from msrest.authentication import ApiKeyCredentials
import time
import json
import os

def main():
    from dotenv import load_dotenv
    global training_client
    global custom_vision_project
    
    try:
        #Get Configuration Settings
        load_dotenv()
        training_endpoint = os.getenv('TrainingEndpoint')
        training_key = os.getenv('TrainingKey')
        project_id = os.getenv('ProjectID')
        
        #authenticate a client for the training API
        credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
        training_client = CustomVisionTrainingClient(training_endpoint, credentials)
        
        #Get the Custom Vision project
        custom_vision_project = training_client.get_project(project_id)
        
        #Upload and tag images
        Upload_Images('images')
    except Exception as ex:
        print(ex)
        
        def Upload_Images(folder):
            print("Uploading images...")
            
            # Get the tags defined in the project
            tags = training_client.get_tags(custom_vision_project.i)
            
            #Create a list of images  with tagged regions
            tagged_images_with_regions = []
            
            #Get the images and tagged regions from the JSON file
            with open('tagged-images.json', 'r') as json_file:
                tagged_images = json.load(json_file)
                for image in tagged_images['files']:
                    #sdsdfsdfsdfsdf
                    
                    
              