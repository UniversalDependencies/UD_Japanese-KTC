# UD_Japanese-KTC

This treebank is produced by automatically converting Kaede treebank,
which is built over the source material of Kyoto corpus.
http://nlp.ist.i.kyoto-u.ac.jp/EN/index.php?Kyoto%20University%20Text%20Corpus


## Recovering data

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
borrowed from the Kyoto Corpus project.

## Spliting

Each data set contains UD annotations for the following sections in Kyoto Corpus.

training: articles from January 1st to 4th and editorials from January to February
development: articles on January 6th and editorials in April
test: articles on January 5th and editorials in March

## Citation

You are encouraged to cite the following paper when you refer to the
Universal Dependencies Japanese Treebank.

Hiroshi Kanayama, Yusuke Miyao, Takaaki Tanaka, Shinsuke Mori,
Masayuki Asahara, and Sumire Uematsu.  A Draft Proposal for Universal
Dependencies Japanese Treebank.  In the Proceedings of the 21st annual
meeting for Gengo Shori Gakkai (The Association for Natural Language
Processing).  2015.  (In Japanese)

## Statistics

Tree count:  9995
Word count:  267631
Token count: 267631
Dep. relations: 30 of which 0 language specific
POS tags: 16
Category=value feature pairs: 0


Documentation status: partial
Data source: automatic
Data available since: UD v1.2
License: CC BY-SA 4.0
Genre: news
Contributors: Asahara, Masayuki; Kanayama, Hiroshi; Matsumoto, Yuji; Miyao, Yusuke; Mori, Shunsuke; Tanaka, Takaaki; Uematsu, Sumire
