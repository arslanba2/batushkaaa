from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.duration = {}
        self.all_nodes = set()

    def add_task(self, task, duration, dependencies):
        self.all_nodes.add(task)
        self.duration[task] = duration
        
        for dep in dependencies:
            self.all_nodes.add(dep)
            self.graph[dep].append(task)
            self.in_degree[task] += 1
        
        if task not in self.in_degree:
            self.in_degree[task] = 0

    def find_critical_operations(self):
        try:
            if not self.all_nodes:
                print("Kritik Yol Analizi: Grafta hiç düğüm yok.")
                return [], {}, {}

            # Her düğüm için süre tanımlandığından emin olalım
            for node in self.all_nodes:
                if node not in self.duration:
                    print(f"Uyarı: '{node}' düğümü için süre tanımlanmamış, 0 varsayılıyor.")
                    self.duration[node] = 0

            # Topological sort
            queue = deque()
            for task in self.in_degree:
                if self.in_degree[task] == 0:
                    queue.append(task)
            
            topological_order = []
            while queue:
                node = queue.popleft()
                topological_order.append(node)
                
                for neighbor in self.graph[node]:
                    self.in_degree[neighbor] -= 1
                    if self.in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            # Topolojik sıralama tüm düğümleri içermiyor mu kontrol et
            if len(topological_order) != len(self.all_nodes):
                print("Uyarı: Topolojik sıralama tüm düğümleri içermiyor - döngü olabilir.")
                missing_nodes = self.all_nodes - set(topological_order)
                topological_order.extend(list(missing_nodes))

            # Calculate earliest start and finish times
            earliest_start = {task: 0 for task in self.all_nodes}
            earliest_finish = {task: 0 for task in self.all_nodes}
            
            for task in topological_order:
                earliest_finish[task] = earliest_start[task] + self.duration[task]
                for neighbor in self.graph[task]:
                    earliest_start[neighbor] = max(earliest_start[neighbor], earliest_finish[task])

            # Calculate latest start and finish times
            max_finish_time = max(earliest_finish.values())
            latest_finish = {task: max_finish_time for task in self.all_nodes}
            latest_start = {task: 0 for task in self.all_nodes}
            
            # Reverse topological order for latest calculations
            for task in reversed(topological_order):
                if not self.graph[task]:  # Eğer bağımlılık yoksa, latest_finish = max_finish_time
                    latest_finish[task] = max_finish_time
                else:
                    latest_finish[task] = min(latest_start[neighbor] for neighbor in self.graph[task])
                
                latest_start[task] = latest_finish[task] - self.duration[task]

            # Identify critical operations
            critical_operations = []
            for task in topological_order:
                if earliest_start[task] == latest_start[task] and earliest_finish[task] == latest_finish[task]:
                    critical_operations.append(task)
                    
            return critical_operations, earliest_start, latest_finish
            
        except Exception as e:
            print(f"Kritik Yol Analizi Hatası: {e}")
            return [], {}, {}
        
# Örnek kullanım
if __name__ == "__main__":
    g = Graph()
    g.add_task('A', 3, [])
    g.add_task('B', 2, ['A'])
    g.add_task('C', 4, ['A'])
    g.add_task('D', 1, ['B', 'C'])
    g.add_task('E', 2, ['C'])
    g.add_task('F', 3, ['D', 'E'])

    critical_operations, earliest_start, latest_finish = g.find_critical_operations()
    
    print("Kritik Operasyonlar:", critical_operations)
    print("En Erken Başlama Zamanları:", earliest_start)
    print("En Geç Tamamlanma Zamanları:", latest_finish)