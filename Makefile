# Simple Makefile for static site generation

.PHONY: build clean serve install help

# Build the static site
build:
	python generate.py

# Clean build artifacts
clean:
	rm -rf dist/

# Install dependencies
install:
	pip install jinja2

# Serve the built site locally (requires Python)
serve:
	cd dist && python -m http.server 8000

# Build and serve
dev: build serve

# Help
help:
	@echo "Available commands:"
	@echo "  make build   - Generate static HTML files"
	@echo "  make clean   - Remove build artifacts"
	@echo "  make serve   - Serve the built site locally"
	@echo "  make dev     - Build and serve"
	@echo "  make install - Install Python dependencies"
	@echo "  make help    - Show this help message"
