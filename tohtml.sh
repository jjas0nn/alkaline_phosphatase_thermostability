jupyter nbconvert *.ipynb
rm -rf html/
mkdir html
mv *.html html/
scp -r html/* jasjen13@redfern.dreamhost.com:jj-jj.xyz/
