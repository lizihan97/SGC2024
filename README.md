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

## Generate Certs, Medals, and Tags

Execute `main.sh` and the following files will be generated. 
```
├── output
│   ├── cert_cop.pdf
│   ├── cert_open.pdf
│   ├── cert_sin.pdf
│   ├── medal.pdf
│   └── tag_competitor.pdf
```

## Generate JPG's for tags
- Make sure the dimension of templates is as required before generating PDF's.
- Convert `output/tag_competitor.pdf` to JPG's and save them in `output/tag_competitor`.
- Convert `templates/template_tag.pdf` to JPG's and save them in `output/tag_template`.
- Edit `rename.sh` to specify the number of competitors and the number of template duplicates.

    ```
    COMPETITOR=216
    TEMPLATE=4
    ORGANIZER=6
    DELEGATE=4
    STAFF=50
    ```
- Run `sh rename.sh`.
- JPG's are saved in `output/tag_all`. File names follow the format of `x000-1.jpg`.

    ```
    c216 for competitor
    d04 for delegate
    o06 for organizer 
    s50 for staff
    t04 for competitor template

    -1 for front
    -2 for back

    280 tags x 2 sides
    ```

## Font
Download fonts for other languages at https://fonts.google.com/noto

## Event Icons
Event icons are available at https://github.com/cubing/icons/tree/main/svgs/event