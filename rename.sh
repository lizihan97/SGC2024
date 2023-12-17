rm -rf output/tag_all
mkdir -p output/tag_all

COMPETITOR=216
TEMPLATE=4
ORGANIZER=6
DELEGATE=4
STAFF=50

for i in $(seq 1 $COMPETITOR); do
    j=$(printf "%.3d" $i)
    f=$(printf "%.3d" $((i*2-1)))
    b=$(printf "%.3d" $((i*2)))
    cp output/tag_competitor/tag_competitor_Page_${f}.jpg output/tag_all/c${j}-1.jpg
    cp output/tag_competitor/tag_competitor_Page_${b}.jpg output/tag_all/c${j}-2.jpg
done

for i in $(seq 1 $TEMPLATE); do
    j=$(printf "%.2d" $i)
    cp output/tag_template/template_tag_Page_1.jpg output/tag_all/t${j}-1.jpg
    cp output/tag_template/template_tag_Page_2.jpg output/tag_all/t${j}-2.jpg
done

for i in $(seq 1 $ORGANIZER); do
    j=$(printf "%.2d" $i)
    cp output/tag_template/template_tag_Page_3.jpg output/tag_all/o${j}-1.jpg
    cp output/tag_template/template_tag_Page_4.jpg output/tag_all/o${j}-2.jpg
done

for i in $(seq 1 $DELEGATE); do
    j=$(printf "%.2d" $i)
    cp output/tag_template/template_tag_Page_5.jpg output/tag_all/d${j}-1.jpg
    cp output/tag_template/template_tag_Page_6.jpg output/tag_all/d${j}-2.jpg
done

for i in $(seq 1 $STAFF); do
    j=$(printf "%.2d" $i)
    cp output/tag_template/template_tag_Page_7.jpg output/tag_all/s${j}-1.jpg
    cp output/tag_template/template_tag_Page_8.jpg output/tag_all/s${j}-2.jpg
done