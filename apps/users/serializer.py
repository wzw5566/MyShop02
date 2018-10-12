# -*- coding: UTF-8 -*-
import re
from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()
