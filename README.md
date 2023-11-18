# SGC2024
For generating certs, medals, and tags.

## Package Requirements
```
pip install -r requirements.txt
```

## Files to Upload

```
.
├── reg.csv
└── templates
    ├── template_cop.pdf
    ├── template_medal.pdf
    ├── template_open.pdf
    ├── template_sin.pdf
    └── template_tag.pdf
```

- Add a `templates` folder that contains templates named as in the folder structure.
- For cop and tags, add `reg.csv` in the project folder. For compulsory columns, please refer to `sample.csv` as a sample.

## Generate Certs

Execute `main.sh` and the following files will be generated. 
```
├── output
│   ├── cert_cop.pdf
│   ├── cert_open.pdf
│   ├── cert_sin.pdf
│   ├── medal.pdf
│   └── tag_competitor.pdf
```

## Font
Download fonts for other languages at https://fonts.google.com/noto

## Event Icons
Event icons are available at https://github.com/cubing/icons/tree/main/svgs/event