variable "additional_tags" {
  type        = map(string)
  description = "Map of additional tags to apply to resources"
  default = {
    "student"  = "pryimak",
    "homework" = "hw"
  }
}



variable "vpc_cidr_block" {
  type        = string
  default     = "10.0.0.0/16"
  description = "VPC CIDR block to use"
}

variable "public_cidr" {
  type        = string
  default     = "10.0.52.0/24"
  description = "Public subnet CIDR"
}

variable "private_cidr" {
  type        = string
  default     = "10.0.66.0/24"
  description = "Private subnet CIDR"
}
