# provider.tf
terraform {
  required_providers {
    airbyte = {
      source  = "airbytehq/airbyte"
      version = "0.2.3"
    }
  }
}

provider "airbyte" {
  username = "airbyte"
  password = "password"
  server_url = "http://localhost:8006/v1"
}