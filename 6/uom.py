import sys, re

def startup(file):
  graph = { 'COM':[] }
  with open(file) as input:
    for line in input:
      line = line.strip()
      objs = re.split("\)", line)
      orbiter = objs[1]
      orbitee = objs[0]
      if orbiter in graph:
        graph[orbiter].append(orbitee)
      else:
        graph[orbiter] = [orbitee]
  
  # direct = countDirectOrbits(graph)
  # indirect = countIndirectOrbits(graph)
  # total = direct + indirect
  # print(total)

  print(bfs(graph, graph["YOU"][0], graph["SAN"][0]))

def countDirectOrbits(graph):
  count = 0
  for k, v in graph.items():
    count += len(v)
  return count

def countIndirectOrbits(graph):
  count = 0
  for k, v in graph.items():
    objs = v.copy()
    while len(objs) > 0:
      cur = objs.pop()
      if cur in graph:
        curOrbits = graph[cur]
        objs.extend(curOrbits)
        count += len(curOrbits)
  return count

def bfs(graph, src, dest):
  for k, v in graph.items():
    for obj in v:
      if obj in graph:
        graph[obj].append(k)
      else:
        graph[obj] = [k]
  
  queue = [src]
  visited = { src }
  dist = { src:0 }

  while len(queue) > 0:
    cur = queue.pop()
    if cur == dest:
      break
    elif (cur in graph):
      curOrbits = graph[cur]
      for obj in curOrbits:
        if (obj not in visited):
          queue.append(obj)
          visited.add(obj)
          dist[obj] = dist[cur] + 1

  return dist[dest]

if __name__ == '__main__':
  startup(sys.argv[1])