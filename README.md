# algoritmo-II-python
Aulas de algoritmo 2 da UNIVESP com Python

## Testes

```bash
pip install -r requirements-dev.txt
pytest            # roda os testes
pytest --cov      # roda os testes com relatorio de cobertura
```

Os scripts das aulas ficam em pastas com espacos no nome, entao os testes os
carregam por caminho com o helper `load_script` em `tests/conftest.py`. Os
scripts de interface grafica (`Semana - 7 - Interface com Python`) abrem uma
janela com `mainloop()` no nivel do modulo e nao sao cobertos.

