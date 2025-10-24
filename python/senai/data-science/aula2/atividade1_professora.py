# ATIVIDADE 2


notas = [[10,10,10],[5,2,3],[5,9,8],[10,0,6]]
nomes = ['Ana','Fernanda', 'Caio', 'Fernando']


ana_media  =  sum(notas[0])/len(notas[0])
fernanda_media = sum(notas[1])/len(notas[1])
caio_media = sum(notas[2])/len(notas[2])
fernando_media =sum( notas[3])/len(notas[2])


print('ANA', ana_media)
print('FERNANDA', fernanda_media)
print('CAIO', caio_media)
print('FERNANDO', fernando_media)


md_alunos =  [ana_media, fernanda_media, caio_media,fernando_media]
maior  =  max(md_alunos)


indice =  md_alunos.index(maior)
print('Aluno com maior media', nomes[indice])


print('Maior media', maior)


media_class = sum(md_alunos)/len(md_alunos)
print('media classe', media_class)