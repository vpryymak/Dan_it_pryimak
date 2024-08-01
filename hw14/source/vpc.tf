resource "aws_vpc" "default" {
  cidr_block = var.vpc_cidr_block

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-vpc"
    },
  )
}


resource "aws_internet_gateway" "ig" {
  vpc_id = aws_vpc.default.id
  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-ig"
    },
  )
}


resource "aws_eip" "nat" {
  vpc        = true
  depends_on = [aws_internet_gateway.ig]
}


resource "aws_nat_gateway" "nat" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public.id

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-nat"
    },
  )
}


resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = var.public_cidr
  map_public_ip_on_launch = true
  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-public"
    },
  )
}


resource "aws_subnet" "private" {
  vpc_id                  = aws_vpc.default.id
  cidr_block              = var.private_cidr
  map_public_ip_on_launch = false

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-private"
    },
  )
}


resource "aws_route_table" "private" {
  vpc_id = aws_vpc.default.id

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-private"
    },
  )
}


resource "aws_route_table" "public" {
  vpc_id = aws_vpc.default.id

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-public"
    },
  )
}

resource "aws_route" "public_internet_gateway" {
  route_table_id         = aws_route_table.public.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.ig.id
}
resource "aws_route" "private_nat_gateway" {
  route_table_id         = aws_route_table.private.id
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id         = aws_nat_gateway.nat.id
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "private" {
  subnet_id      = aws_subnet.private.id
  route_table_id = aws_route_table.private.id
}

resource "aws_security_group" "public" {
  name        = "${var.additional_tags["student"]}-public-sg"
  description = "Public security group"
  vpc_id      = aws_vpc.default.id
  ingress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-public-sg"
    },
  )
}

resource "aws_security_group" "private" {
  name        = "${var.additional_tags["student"]}-private-sg"
  description = "Private security group"
  vpc_id      = aws_vpc.default.id
  ingress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = [aws_subnet.public.cidr_block]
  }

  egress {
    from_port   = "0"
    to_port     = "0"
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    var.additional_tags,
    {
      Name = "${var.additional_tags["student"]}-private-sg"
    },
  )
}
