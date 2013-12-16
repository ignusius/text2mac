<h1>TEXT2MAC</h1>

This program convert text to MAC-style.

<b>example command: example command: text2mac file1.txt out_file1.txt</b>

<b>file1.txt:</b>
**********
<p>24A921418907</p>
<p>24A92141891D</p>
<p>24A9214189F4</p>
**********
<b>out_file1.txt:</b>
**********
<p>24:A9:21:41:89:07</p>
<p>24:A9:21:41:89:1D</p>
<p>24:A9:21:41:89:F4</p>
**********
<h3>Options:</h3>
<p>text2mac f1.txt f2.txt  [upper,lower] [2,3],[:,.] 'text ' ' text'</p>
<b>example: text2mac f1.txt f2.txt  lower 3 . 'text ' ' text'</b>
*********
<b>f2.txt</b>
<p>text1 24a.921.418.907 text2</p>
<p>text1 24a.921.418.91d text2</p>
<p>text1 24a.921.418.9f4 text2</p>
