#!/bin/bash
#
# 2018-07-09
# Rename the image files I download to the format:
#   YYYYMMDD_HHMMSS-originalname-image_dims.XXX
#
echo
echo SCRIPT TO RENAME IMAGES USING EXIFTOOL
echo


    exiftool '-FileName<CreateDate' -d %Y%m%d_%H%M%S-%%f.%%e *.JPG;
    exiftool '-FileName<CreateDate' -d %Y%m%d_%H%M%S-%%f.%%e *.jpg;
    exiftool '-FileName<CreateDate' -d %Y%m%d_%H%M%S-%%f.%%e *.JPEG;
    exiftool '-FileName<CreateDate' -d %Y%m%d_%H%M%S-%%f.%%e *.PNG;
    exiftool '-FileName<CreateDate' -d %Y%m%d_%H%M%S-%%f.%%e *.MOV;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e I*.JPG;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e I*.jpg;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e i*.JPG;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e i*.jpg;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e P*.JPG;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e P*.jpg;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e I*.PNG;
    exiftool '-FileName<FileCreateDate' -d %Y%m%d_%H%M%S-%%f.%%e I*.png;
    exiftool '-FileName<%f-$imagesize.%e' 20*.JPG;
    exiftool '-FileName<%f-$imagesize.%e' 20*.jpg;
    exiftool '-FileName<%f-$imagesize.%e' 20*.JPEG;
    exiftool '-FileName<%f-$imagesize.%e' 20*.jpeg;
    exiftool '-FileName<%f-$imagesize.%e' 20*.PNG;
    exiftool '-FileName<%f-$imagesize.%e' 20*.png;
    exiftool '-FileName<%f-$imagesize.%e' 20*.MOV;
    exiftool '-FileName<%f-$imagesize.%e' 20*.mov;



echo COMPLETE
