# Ambientes Virtuais

Interpretador do Python ISOLADO do python global.

## Comandos

1. Criando ambiente virtual

```powershell
python -m venv <nome_do_ambiente>
```

2. Ativando o ambiente virtual

- Windows
```powershell
<nome_do_ambiente>\Scripts\activate
```

- Linux
```bash
source <nome_do_ambiente>/bin/activate
```

**OBS:** Caso dê erro ao ativar o ambiente virtual no VSCode, execute o comando abaixo no PowerShell
```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```