#!/usr/bin/env python
# -*- coding: utf8 -*-
#
# author: harald schilly <harald@schil.ly>

from PIL import Image, ImageDraw
import random, math

### Parameters, try to change nb_edges!

#size      = 256, 256
size      = 512, 512
nb_edges  = 5
edges     = []
nb_points = 1000000 # how many to plot 

### code starts here

img = Image.new("RGB", size, "white")
draw = ImageDraw.Draw(img)

mp  = size[0]/2, size[1]/2
rad = min(size[0], size[1])/2 - 1

for i in range(nb_edges):
  r = 2 * math.pi * (float(i) / nb_edges)
  edge = mp[0] + math.sin(r) * rad, mp[1] - math.cos(r) * rad
  print r, edge
  edges.append(edge)

draw.point(edges, fill=0)

def midpoint(p1, p2):
  return tuple((p1[_]+p2[_])/2.0 for _ in range(2))

p = random.choice(edges)
pnts = {}
max_cnt = 0
inc_last, inc = 0, nb_points / 30
for i in range(nb_points):
  p = midpoint(p, random.choice(edges))
  p_rnd = int(p[0]), int(p[1])
  pnts[p_rnd] = cnt = pnts.get(p_rnd, 0) + 1
  max_cnt = max(max_cnt, cnt)
  if i > inc_last:
    inc_last += inc
    print 'progress: %.2f%%' % (float(i)/nb_points * 100)

print "finished point sampling, now plotting"

gradients = '059e'
ngradients = len(gradients) - 1

inc_last, inc = 0, len(pnts) / 7 
for idx, (pnt, cnt) in enumerate(pnts.iteritems()):
  i = gradients[-int(ngradients * (float(cnt) / max_cnt))]
  col = '#%(i)s%(i)s%(i)s' % { 'i' : i }
  draw.point(pnt, fill = col)
  if idx > inc_last:
    inc_last += inc
    print 'progress: %.2f%%' % (float(idx)/len(pnts)* 100)


img.save("nsierp.png", "PNG")

