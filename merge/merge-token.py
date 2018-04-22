#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


# pattern for a line showing sentence id 
sid_pat = re.compile(ur'^#\s+S-ID:\s*([0-9]+-[0-9]+)')

offset_prefix = 'Offset='

def main():
    if len(sys.argv) < 3:
        show_usage(sys.argv[0])
        sys.exit(1)
    text_file  = sys.argv[1]
    conll_file = sys.argv[2]

    conll_f = open(conll_file, 'r')
    text_f = open(text_file, 'r')

    conll_line = []
    for line in conll_f:
        line = line.decode('utf-8').rstrip('\n')

        if len(line) > 0:
            conll_line.append(line)
        else: # end of sentence in conll
            # check sentence id
            conll_id = get_conll_sid(conll_line)

            if conll_id == None: pass
            else:
                # search text_file for the same id
                text_id, sent = None, None

                for text_l in text_f:
                    text_l = text_l.decode('euc-jp').rstrip('\n')

                    sid_match = sid_pat.search(text_l)
                    if sid_match and sid_match.group(1) == conll_id:
                        text_id = sid_match.group(1)
                    elif text_id != None and not text_l.startswith('#'):
                        sent = text_l
                        break

                if text_id != None and sent != None:
                    print_token(sent, conll_line)
                    print

            conll_line = []

    conll_f.close()
    text_f.close()


def get_conll_sid(lines):
    if len(lines) <= 0:
        return None
    match = sid_pat.search(lines[0])
    if not match:
        sys.stderr.write('the first line must be a comment line showing sentence id')
        sys.exit()
    return match.group(1)


def print_token(sent, deps):
    if len(deps) <= 0:
        return
    match = sid_pat.search(deps[0])
    if not match:
        sys.stderr.write('the first line must be a comment line showing sentence id')
        sys.exit()
    
    print deps[0]
    for d in deps[1:]:
        tid, token, lemma, pos, pos2, feat, head, dep, dep2, misc = d.split('\t', 9)

        offset_found = [m for m in misc.split('|') if m.startswith(offset_prefix)]
        assert len(offset_found) > 0
        start, end = offset_found[0][len(offset_prefix):].partition('-')[::2]
        start, end = int(start), int(end)

        token = sent[start:end]
        if lemma == '_': lemma = token

        other_misc = [m for m in misc.split('|') if not m.startswith(offset_prefix)]
        if len(other_misc) < 1:
            misc = '_'
        else:
            misc = '|'.join(other_misc)

        print '\t'.join([tid, token, lemma, pos, pos2, feat, head, dep, dep2, misc]).encode('utf-8')

def show_usage(name):
    print '{0} text dep'.format(name)


main()

