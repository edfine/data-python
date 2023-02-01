from typing import Dict, Set

class Directory:
    """Keep a mapping of hosts to addresses."""
    __hosts: Dict[str, Set[str]]
    
    def __init__(self):
        self.__hosts = {}
        
    def __repr__(self) -> str:
        return f'<Directory of {len(self.__hosts)} hosts>'
        
    def __str__(self) -> str:
        lines = [f'Directory of {len(self.__hosts)} hosts']
        for host, addresses in self.__hosts.items():
            lines.append(f' - {host} => {addresses}')
        return '\n'.join(lines)
        
    def add_mapping(self, name: str, address: str) -> None:
        if name not in self.__hosts:
            self.__hosts[name] = set()
        self.__hosts[name].add(address)
        
    def remove_mapping(self, name: str, address: str) -> None:
        if name in self.__hosts:
            self.__hosts[name].discard(address)
            
    def resolve(self, name: str) -> Set[str]:
        if name in self.__hosts:
            return self.__hosts[name]
        else:
            return 'NXDOMAIN'
