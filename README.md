<h1>TEXT2MAC</h1>

This program convert text to MAC-style.

<b>example command: text2mac file1.txt out_file.txt 'text_before_mac ' ' text_after_mac'</b>

<b>file1.txt:</b>
**********
<p>24A921418907</p>
<p>24A92141891D</p>
<p>24A9214189F4</p>
**********
<b>out_file1.txt:</b>
**********
<p>text_before_mac 24:A9:21:41:89:07 text_after_mac</p>
<p>text_before_mac 24:A9:21:41:89:1D text_after_mac</p>
<p>text_before_mac 24:A9:21:41:89:F4 text_after_mac</p>
**********
<h3>Options:</h3>
<p>text2mac f1.txt f2.txt 'text ' ' text' [upper,lower] [2,3],[:,.]</p>
<b>example: text2mac f1.txt f2.txt 'text ' ' text' lower 3 .</b>
*********
<b>f2.txt</b>
<p>text 24a.921.418.907 text</p>
<p>text 24a.921.418.91d text</p>
<p>text 24a.921.418.9f4 text</p>

