import os

# 1. Definição do conteúdo do index.yaml
# Este arquivo serve como menu principal para o girus-cli
# Segue o modelo: https://github.com/badtuxx/girus-cli?tab=readme-ov-file#indexyaml
index_yaml = """
apiVersion: v1
generated: "2024-03-20T10:00:00Z"
entries:
  lab-name:
    - name: "01 - Instalação da Gateway API"
      version: "1.0.0"
      description: "Instalação dos CRDs padrão da Gateway API e do Envoy Gateway."
      created: "2025-11-11T11:50:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/01-instalacao/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - setup
        - install
        - gateway api

    - name: "02 - Exposição com HTTPRoute"
      version: "1.0.0"
      description: "Exposição de serviços HTTP e roteamento por path."
      created: "2025-11-11T12:00:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/02-httproute/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - http
        - routing

    - name: "03 - Exposição com TCPRoute"
      version: "1.0.0"
      description: "Exposição de serviços TCP (ex: Redis)."
      created: "2025-11-11T12:10:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/03-tcproute/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - tcp
        - redis

    - name: "04 - Exposição com UDPRoute"
      version: "1.0.0"
      description: "Exposição de serviços UDP."
      created: "2025-11-11T12:20:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/04-udproute/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - udp

    - name: "05 - Websockets"
      version: "1.0.0"
      description: "Configuração de suporte a Websockets via HTTPRoute."
      created: "2025-11-11T12:30:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/05-websocket/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - websocket
        - http

    - name: "06 - TLSRoute (Passthrough)"
      version: "1.0.0"
      description: "Roteamento TLS Passthrough usando SNI."
      created: "2025-11-11T12:40:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/06-tlsroute/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - tls
        - security

    - name: "07 - GRPCRoute"
      version: "1.0.0"
      description: "Roteamento nativo de gRPC."
      created: "2025-11-11T12:50:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/07-grpcroute/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - grpc

    - name: "08 - GAMMA (Mesh)"
      version: "1.0.0"
      description: "Gateway API para Service Mesh (Leste-Oeste)."
      created: "2025-11-11T13:00:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/08-mesh-gamma/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - mesh
        - gamma

    - name: "09 - Debug e Troubleshooting"
      version: "1.0.0"
      description: "Técnicas de debug, status conditions e logs."
      created: "2025-11-11T13:10:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/09-debug/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - debug
        - troubleshooting

    - name: "10 - Monitoramento com Datadog"
      version: "1.0.0"
      description: "Integração com Datadog para métricas e logs."
      created: "2025-11-11T13:20:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/10-datadog/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - datadog
        - monitoring

    - name: "11 - Monitoramento LGTM (Grafana)"
      version: "1.0.0"
      description: "Integração com stack LGTM (Grafana Labs)."
      created: "2025-11-11T13:30:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/11-grafana-stack/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - grafana
        - loki
        - tempo
        - prometheus

    - name: "12 - Monitoramento VictoriaMetrics"
      version: "1.0.0"
      created: "2025-11-11T13:40:00Z"
      url: "https://raw.githubusercontent.com/aeciopires/mylabs-for-girus-cli/refs/heads/main/gateway-api/12-victoria-stack/lab.yaml"
      digest: "sha256:hash-do-arquivo"
      maintainers:
        - "Aecio Pires"
      keywords: 
        - victoriametrics
        - monitoring
"""

# 2. Dicionário contendo todos os arquivos e seus conteúdos
# A chave é o caminho do arquivo (relativo ao diretório de execução)
files_content = {
    # Arquivo de índice na raiz
    "index.yaml": index_yaml,

    # README global
    "README.md": """# Laboratórios Gateway API para girus-cli

Pacote de laboratórios práticos para aprendizado de Kubernetes Gateway API.

## Como usar

Siga as instruções do post: CHANGE_HERE
""",

    # --- LAB 01: Instalação ---
    "01-instalacao/lab.yaml": """title: "01 - Instalação da Gateway API"
description: "Neste laboratório, vamos instalar os CRDs padrão da Gateway API e um Gateway Controller (Envoy Gateway)."
steps:
  - title: "Instalar CRDs da Gateway API"
    text: |
      A Gateway API é baseada em CRDs (Custom Resource Definitions).
      Execute o comando abaixo para instalar os CRDs padrão (v1.2.0):
      
      `kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.0/standard-install.yaml`
    verify: "kubectl get crd gateways.gateway.networking.k8s.io"

  - title: "Instalar o Envoy Gateway (Controller)"
    text: |
      Precisamos de um controlador para implementar as regras. Usaremos o Envoy Gateway.
      Instale via Helm:
      
      `helm install eg oci://docker.io/envoyproxy/gateway-helm --version v0.0.0-latest -n envoy-gateway-system --create-namespace`
      
      Ou aguarde a instalação se já tiver aplicado.
    verify: "kubectl get pods -n envoy-gateway-system -l control-plane=envoy-gateway"

  - title: "Verificar GatewayClass"
    text: |
      O Envoy Gateway cria uma GatewayClass padrão chamada `eg`. Verifique se ela existe.
    verify: "kubectl get gatewayclass eg"
""",

    # --- LAB 02: HTTPRoute ---
    "02-httproute/lab.yaml": """title: "02 - Exposição com HTTPRoute"
description: "Aprenda a expor microsserviços HTTP e fazer roteamento baseado em path."
steps:
  - title: "Deploy da Aplicação de Teste"
    text: |
      Crie um deployment simples chamado `httpbin` (porta 8000) e seu serviço.
      Você pode usar o arquivo `solucao/apps.yaml` se desejar.
    verify: "kubectl get svc httpbin"

  - title: "Criar o Gateway"
    text: |
      Crie um Gateway que utilize a `gatewayClassName: eg` e escute na porta 80 (protocolo HTTP).
    verify: "kubectl get gateway my-gateway"

  - title: "Criar o HTTPRoute"
    text: |
      Crie um `HTTPRoute` que direcione todo o tráfego `/` para o serviço `httpbin` na porta 8000.
      Associe este roteamento ao gateway `my-gateway`.
    verify: "kubectl get httproute httpbin-route"

  - title: "Testar Acesso"
    text: |
      Obtenha o IP do Gateway e faça uma requisição curl.
      Dica: `kubectl get gateway my-gateway -o jsonpath='{.status.addresses[0].value}'`
    verify: "kubectl get gateway my-gateway -o jsonpath='{.status.addresses[0].value}'"
""",
    "02-httproute/solucao/apps.yaml": """apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin
spec:
  replicas: 1
  selector:
    matchLabels:
      app: httpbin
  template:
    metadata:
      labels:
        app: httpbin
    spec:
      containers:
      - name: httpbin
        image: kennethreitz/httpbin
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: httpbin
spec:
  selector:
    app: httpbin
  ports:
  - port: 8000
    targetPort: 80
""",
    "02-httproute/solucao/gateway.yaml": """apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
spec:
  gatewayClassName: eg
  listeners:
  - name: http
    protocol: HTTP
    port: 80
""",
    "02-httproute/solucao/route.yaml": """apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: httpbin-route
spec:
  parentRefs:
  - name: my-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /
    backendRefs:
    - name: httpbin
      port: 8000
""",

    # --- LAB 03: TCPRoute ---
    "03-tcproute/lab.yaml": """title: "03 - Exposição com TCPRoute"
description: "Roteamento de tráfego TCP não-HTTP (ex: Redis)."
steps:
  - title: "Deploy do Redis"
    text: |
      Faça o deploy de um Redis simples e seu Service na porta 6379.
    verify: "kubectl get svc redis"

  - title: "Atualizar Gateway para TCP"
    text: |
      Edite seu Gateway para adicionar um novo listener na porta 6379 com protocolo TCP.
      Dica: Use `kubectl edit gateway my-gateway`.
    verify: "kubectl get gateway -o json | grep 6379"

  - title: "Criar TCPRoute"
    text: |
      Crie um manifesto usando o kind `TCPRoute`.
      Aponte para o service `redis` e referencie o listener TCP do gateway.
    verify: "kubectl get tcproute redis-route"
""",
    "03-tcproute/solucao/tcp-route.yaml": """apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TCPRoute
metadata:
  name: redis-route
spec:
  parentRefs:
  - name: my-gateway
    sectionName: tcp
  rules:
  - backendRefs:
    - name: redis
      port: 6379
""",

    # --- LAB 04: UDPRoute ---
    "04-udproute/lab.yaml": """title: "04 - Exposição com UDPRoute"
description: "Roteamento de tráfego UDP."
steps:
  - title: "Deploy App UDP"
    text: |
      Vamos usar uma imagem `agnhost` para servir como servidor de eco UDP na porta 8081.
      Crie o deployment e o service.
    verify: "kubectl get svc udp-echo"

  - title: "Configurar Listener UDP"
    text: |
      Adicione um listener ao seu Gateway na porta 8081 com protocolo UDP.
    verify: "kubectl get gateway my-gateway -o yaml"

  - title: "Criar UDPRoute"
    text: |
      Crie um recurso `UDPRoute` apontando para o service `udp-echo`.
    verify: "kubectl get udproute udp-echo-route"
""",

    # --- LAB 05: Websocket ---
    "05-websocket/lab.yaml": """title: "05 - Websockets"
description: "Websockets são tratados nativamente pelo HTTPRoute."
steps:
  - title: "Deploy Websocket App"
    text: |
      Deploy de uma aplicação de eco websocket (ex: jmalloc/echo-server).
    verify: "kubectl get svc websocket-app"

  - title: "Criar HTTPRoute para Websocket"
    text: |
      O Gateway API trata Websocket como HTTP.
      Crie um `HTTPRoute` para o service websocket na porta 80.
    verify: "kubectl get httproute ws-route"
""",

    # --- LAB 06: TLSRoute ---
    "06-tlsroute/lab.yaml": """title: "06 - TLSRoute (Passthrough)"
description: "Roteamento baseado em SNI onde a terminação TLS ocorre na aplicação."
steps:
  - title: "Deploy App Seguro"
    text: |
      Para este lab, crie um service `my-secure-app` (simulado).
    verify: "kubectl get svc my-secure-app || kubectl create svc clusterip my-secure-app --tcp=8443"

  - title: "Configurar Gateway TLS Passthrough"
    text: |
      Adicione um listener ao Gateway na porta 443, Protocolo TLS, Mode Passthrough.
      Configure o hostname como `secure.example.com`.
    verify: "kubectl get gateway my-gateway -o yaml"

  - title: "Criar TLSRoute"
    text: |
      Crie um `TLSRoute` que use o SNI `secure.example.com` e direcione para o serviço da aplicação.
    verify: "kubectl get tlsroute secure-route"
""",

    # --- LAB 07: GRPCRoute ---
    "07-grpcroute/lab.yaml": """title: "07 - GRPCRoute"
description: "Roteamento nativo de gRPC."
steps:
  - title: "Deploy gRPC App"
    text: |
      Deploy de um servidor gRPC (ex: yages).
    verify: "kubectl get svc yages"

  - title: "Criar GRPCRoute"
    text: |
      Crie um recurso `GRPCRoute`.
      Faça o match pelo serviço `yages.Echo` e método `Ping`.
    verify: "kubectl get grpcroute yages-route"
""",

    # --- LAB 08: GAMMA (Mesh) ---
    "08-mesh-gamma/lab.yaml": """title: "08 - GAMMA (Gateway API for Mesh)"
description: "Uso do HTTPRoute para tráfego Leste-Oeste (Service to Service)."
steps:
  - title: "Pré-requisito: CRDs"
    text: |
      Verifique se os CRDs experimentais do Gateway API estão instalados.
    verify: "kubectl get crd httproutes.gateway.networking.k8s.io"

  - title: "Deploy Servidor"
    text: |
      Deploy de um service chamado `server`.
    verify: "kubectl get svc server || kubectl create svc clusterip server --tcp=80"

  - title: "Criar HTTPRoute para Mesh"
    text: |
      Para GAMMA, o `parentRef` do HTTPRoute deve apontar para um **Service** (não Gateway).
      Crie um HTTPRoute onde `parentRef` seja o Service `server`.
    verify: "kubectl get httproute mesh-route"
""",

    # --- LAB 09: Debug ---
    "09-debug/lab.yaml": """title: "09 - Debug e Troubleshooting"
description: "Diagnóstico de problemas usando Status Conditions e Events."
steps:
  - title: "Verificar Status da GatewayClass"
    text: |
      Verifique se a GatewayClass foi aceita pelo controller.
      Procure por `status: conditions: type: Accepted` sendo `True`.
    verify: "kubectl get gatewayclass eg -o jsonpath='{.status.conditions[?(@.type==\"Accepted\")].status}'"

  - title: "Debugar Gateway"
    text: |
      Use o comando describe para ver eventos do Gateway.
      `kubectl describe gateway my-gateway`
    verify: "kubectl get gateway my-gateway"

  - title: "Debugar Rota (Parents Status)"
    text: |
      Verifique o status da rota. A Gateway API reporta o status por 'Parent'.
      Execute: `kubectl describe httproute <nome-da-rota>`
      Analise a seção `Status > Parents > Conditions`.
    verify: "kubectl get httproute"

  - title: "Logs do Controller"
    text: |
      Se tudo falhar, verifique os logs do pod do Envoy Gateway.
      `kubectl logs -n envoy-gateway-system -l control-plane=envoy-gateway`
    verify: "kubectl get pods -n envoy-gateway-system"
""",

    # --- LAB 10: Datadog ---
    "10-datadog/lab.yaml": """title: "10 - Monitoramento com Datadog"
description: "Configuração de monitoramento e links para dashboards."
steps:
  - title: "Habilitar Métricas no Envoy"
    text: |
      No `EnvoyProxy` config, habilite a telemetria prometheus.
      Verifique a documentação do Datadog: [Datadog Envoy Integration](https://docs.datadoghq.com/integrations/envoy/)
    verify: "kubectl get crd envoyproxies.gateway.envoyproxy.io"

  - title: "Annotations de Autodiscovery"
    text: |
      Adicione annotations ao Pod do Envoy para o agente Datadog:
      `ad.datadoghq.com/envoy.instances: '[{"openmetrics_endpoint": "http://%%host%%:19001/stats/prometheus"}]'`
    verify: "echo 'Configuração revisada'"

  - title: "Acessar Dashboards"
    text: |
      Acesse os dashboards recomendados:
      - [Monitor: High 5xx Rate](https://app.datadoghq.com/monitors/recommended)
      - [Dashboard: Envoy Overview](https://app.datadoghq.com/dash/integration/envoy)
      Confirme que acessou os links.
    verify: "echo 'Links acessados'"
""",

    # --- LAB 11: Grafana Stack ---
    "11-grafana-stack/lab.yaml": """title: "11 - Monitoramento LGTM (Grafana)"
description: "Prometheus, Grafana, Loki e Tempo."
steps:
  - title: "Configurar ServiceMonitor"
    text: |
      Crie um `ServiceMonitor` apontando para a porta 19001 do Envoy.
      Certifique-se que o Prometheus Operator está rodando.
    verify: "kubectl get crd servicemonitors.monitoring.coreos.com || echo 'CRD missing'"

  - title: "Importar Dashboards"
    text: |
      Importe os seguintes IDs no Grafana:
      - **11113**: [Envoy Global](https://grafana.com/grafana/dashboards/11113-envoy-global/)
      - **6693**: [Envoy Proxy](https://grafana.com/grafana/dashboards/6693-envoy-proxy/)
    verify: "echo 'Dashboards importados'"

  - title: "Logs e Traces"
    text: |
      Configure o envio de logs para Loki e traces OTLP para o Tempo.
      Use o `AccessLog` config do Envoy Gateway.
    verify: "echo 'Configuração verificada'"
""",

    # --- LAB 12: VictoriaMetrics ---
    "12-victoria-stack/lab.yaml": """title: "12 - Monitoramento VictoriaMetrics"
description: "Alta performance com VictoriaMetrics Stack."
steps:
  - title: "Configurar VMPodScrape"
    text: |
      Utilize o `VMPodScrape` para coletar métricas da porta 19001.
      Link: [VictoriaMetrics Operator](https://docs.victoriametrics.com/operator/quick-start.html)
    verify: "kubectl get crd vmpodscrapes.operator.victoriametrics.com || echo 'CRD missing'"

  - title: "VictoriaLogs e Dashboards"
    text: |
      Configure o envio de logs para o VictoriaLogs.
      No Grafana, utilize o datasource VictoriaMetrics e use os mesmos dashboards do Envoy (ID 11113).
    verify: "echo 'Setup concluído'"
"""
}

def create_labs_on_disk():
    # Obtém o diretório atual de execução
    base_dir = os.getcwd()

    for file_path, content in files_content.items():
        # Cria o caminho completo para o arquivo
        full_path = os.path.join(base_dir, file_path)
        
        # Garante que o diretório pai existe
        dir_name = os.path.dirname(full_path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        # Escreve o conteúdo no arquivo
        # Usa encoding utf-8 para garantir que acentos funcionem
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip())
            
    print(f"Laboratórios criados com sucesso em: {base_dir}")
    print(f"Total de arquivos gerados: {len(files_content)}")
    print("Execute 'girus lab start .' para iniciar.")

if __name__ == "__main__":
    create_labs_on_disk()
