# AWStack Training Serverless - Découverte d'AWS par la pratique

This repository contains a demo AWS serverless application (using AWS lambada and other services).

It was inscpired by the demo app build during the training session organized by stack labs early 2019.

> Découvrez les **avantages de l'architecture serverless** pour :
>
>- développer des applications rapidement
>- se focaliser sur le développement et non le déploiement
>- améliorer la productivité et l'agilité de l'équipe
>- optimiser le coût et les performances
>Ainsi, vous testerez **les services fourni par AWS au travers d’exemples et d'ateliers (Hands-on)**.
>
>**Les techno abordés** : #AWS S3 #API Gateway #Lambda #DynamoDB #Step Functions #X-Ray #SNS

## The demo application

This applicaiton allows a user to trigger image recognition and automatic thunbnail generation when an image is uploaded to an S3 bucket.

## Usage

Install serveless framework

This application is made out of several services that depend on each other. You have to deploy the services in the right order to avoid errors related to theses dependencies.

```bash
# reference your own profile (perso-adminolive here as declared in ~/.aws/credentials)

# Deploy first service
cd multiple-services/hands-on-1_uploads
serverless deploy -v --aws-profile perso-adminolive

# Deploy second service
cd multiple-services/hands-on-2_py-aws-lambda-presigned-url-template
serverless deploy -v --aws-profile perso-adminolive

# 3rd service....

```

## Organization


