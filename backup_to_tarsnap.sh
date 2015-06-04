#!/bin/bash

tarsnap -cf documents-$(date +%Y-%m-%d) /home/ben/documents
tarsnap -cf code-$(date +%Y-%m-%d) /home/ben/code
