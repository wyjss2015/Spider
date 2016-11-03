egrep '1	|2	|3	|4	|5	' Web开发典藏大系.txt > temp
sed -i 's/5	/好评   /' temp
sed -i 's/4	/好评   /' temp
sed -i 's/3	/中评   /' temp
sed -i 's/2	/中评   /' temp
sed -i 's/1	/差评   /' temp
