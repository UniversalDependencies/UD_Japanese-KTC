# UD_Japanese-KTC

This is a package of the Japanese Corpora of Universal Dependencies.

The data is provided in the CoNLL format, but original texts are
stripped off due to the license issue.  In order to recover the data
with original texts, you need the corpus of Mainichi Shinbun 1995 (the
same set of data for Kyoto Corpus).  The Mainichi Shinbun data can be
obtained from Nichigai Associates:

http://www.nichigai.co.jp/sales/mainichi/mainichi-data.html

The corpus is obtained by running the following command:

./autoconv -d MAINICHI_DIR

where `MAINICHI_DIR` denotes the directory of the files of Mainichi
Shinbun 1995.  In order to run this command, you need Perl and
Python.

The program for extracting texts from Mainichi Shinbun 1995 is
borrowed from the Kyoto Corpus project.  See the following page for
details.

http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?Kyoto%20University%20Text%20Corpus


Documentation status: partial
Data source: automatic
Data available since: UD v1.2
License: CC BY-SA 4.0
Genre: news
Contributors: Asahara, Masayuki; Kanayama, Hiroshi; Matsumoto, Yuji; Miyao, Yusuke; Mori, Shunsuke; Tanaka, Takaaki; Uematsu, Sumire
