terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.83.0"
    }
  }
  required_version = ">= 1.6.0"
}

provider "azurerm" {
  features {}
  skip_provider_registration = true
}

locals {
  location   = "Brazil South"
  app_suffix = "tcc-api"
}

resource "azurerm_resource_group" "rg" {
  name     = "${local.app_suffix}-resource-group"
  location = local.location
}

resource "azurerm_service_plan" "sp" {
  name                = "${local.app_suffix}-plan"
  location            = local.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_linux_web_app" "app" {
  name                = "${local.app_suffix}-deployment"
  service_plan_id     = azurerm_service_plan.sp.id
  resource_group_name = azurerm_resource_group.rg.name
  location            = local.location



  site_config {
    always_on        = false
    app_command_line = "python3.11 -u ./app/main.py"

    application_stack {
      python_version = "3.11"
    }
  }

  logs {
    application_logs {
      file_system_level = "Verbose"
    }
    detailed_error_messages = true
    failed_request_tracing  = true
    http_logs {
      file_system {
        retention_in_days = 7
        retention_in_mb   = 35
      }
    }
  }
}

resource "azurerm_app_service_source_control" "app_sc" {
  app_id                 = azurerm_linux_web_app.app.id
  repo_url               = "https://github.com/VitorCorreaSilva/tcc-api"
  branch                 = "main"
  use_manual_integration = true
}
