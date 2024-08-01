terraform {
  required_version = "~> 1.9.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0.5"
    }
  }
  backend "local" {
    path = "terraform.tfstate"
  }
}


provider "aws" {
  region = "us-east-1"
}
