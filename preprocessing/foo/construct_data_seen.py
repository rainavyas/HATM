import numpy as np
seed=1004
np.random.seed(seed)


for i in xrange(10):
  with open('SCDE_questions_merged_fold'+str(i)+'_seen.txt', 'r') as u:
   with open('SCDE_data_fold'+str(i)+'_seen.txt', 'r') as s:
    with open('neg_data_prompts_seen_fold'+str(i), 'w') as w:
     with open('neg_questions_prompts_seen_fold'+str(i), 'w') as g:
      with open('neg_targets_prompts_seen_fold'+str(i), 'w') as d:
       with open('pos_targets_prompts_seen_fold'+str(i), 'w') as p:
          slines = s.readlines()
          ulines = u.readlines()
          length = len(ulines)

          l=0
          while l < length*10:
            ulines_shuf = np.random.permutation(ulines)
            for uline, sline, line in zip(ulines, slines, ulines_shuf):
                  if l >= length*10:
#                       print 'break'
                        break
                  else:
                    if uline==line:
#                     print "pass",i
                      pass
                    else:
                      l+=1
                      w.write(sline)
                      d.write('0\n')
                      g.write(line)
          for j in xrange(length*10):
                p.write('1\n')

#for i in xrange(10):
#  with open('SCDE_data_fold'+str(i)+'_unseen.txt', 'r') as u:
#    with open('SCDE_data_fold'+str(i)+'_seen.txt', 'r') as s:
#     with open('neg_data_prompts_balanced_fold'+str(i), 'w') as g:
#         slines = s.readlines()
#         ulines = u.readlines()
#          ulines_shuf = np.random.permutation(ulines)

#         for line in slines[0:lens[i]/2]:
#               g.write(line)
#         l=lens[i]/2
#         print l
#         for sline, line in zip(ulines, ulines_shuf):
#               if l >= lens[i]:
#                       print 'break'
#                       break
#               else:
#                 if sline==line:
#                   pass
#                 else:
#                   l+=1
#                   g.write(line)

#for i in xrange(10):
#  with open('SCDE_questions_merged_fold'+str(i)+'_unseen.txt', 'r') as f:
#   with open('SCDE_questions_merged_fold'+str(i)+'_unseen_cut.txt', 'w') as g:
#     with open('new_targets_prompts_seen_fold'+str(i), 'w') as d:
#       with open('pos_targets_prompts_unseen_fold'+str(i), 'w') as p:
#        lines = f.readlines()
#        for line in lines[0:lens[i]]:
#               d.write('0\n')
#               p.write('1\n')
#               g.write(line)
