"""
💰 Assistente Financeiro Virtual com IA Generativa
Desafio de Projeto DIO — Construa seu Assistente Virtual com IA
Autora: Thayná Batista da Silva
Curso: Análise e Desenvolvimento de Sistemas — Faculdade Senac Recife-PE
"""

import os
import json
from openai import OpenAI
from datetime import datetime

# ──────────────────────────────────────────────
# CONFIGURAÇÃO
# ──────────────────────────────────────────────

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Você é a FIN, uma assistente financeira virtual inteligente, empática e didática.
Seu objetivo é ajudar usuários brasileiros a entender melhor suas finanças pessoais.

SUAS CAPACIDADES:
- Responder perguntas sobre educação financeira com linguagem clara e acessível
- Explicar produtos financeiros (CDB, Tesouro Direto, fundos, poupança, etc.)
- Realizar e explicar cálculos financeiros (juros simples, compostos, financiamentos)
- Dar dicas de planejamento financeiro e controle de gastos
- Responder FAQs sobre bancos, cartões, crédito e investimentos

REGRAS IMPORTANTES:
- Nunca forneça recomendações de investimento específicas ou garantias de retorno
- Sempre reforce que decisões financeiras importantes devem consultar um profissional certificado
- Use exemplos práticos com valores em reais (R$)
- Seja sempre positivo, encorajador e didático
- Mantenha contexto da conversa para respostas mais personalizadas
- Use emojis moderadamente para tornar a conversa mais amigável

IDIOMA: Sempre responda em português brasileiro.
"""

# ──────────────────────────────────────────────
# CÁLCULOS FINANCEIROS
# ──────────────────────────────────────────────

def calcular_juros_compostos(principal: float, taxa_mensal: float, meses: int) -> dict:
    """Calcula juros compostos e retorna detalhamento."""
    montante = principal * ((1 + taxa_mensal / 100) ** meses)
    juros = montante - principal
    return {
        "principal": principal,
        "taxa_mensal": taxa_mensal,
        "meses": meses,
        "montante_final": round(montante, 2),
        "juros_total": round(juros, 2),
        "rendimento_percentual": round((juros / principal) * 100, 2),
    }


def calcular_parcela_financiamento(valor: float, taxa_mensal: float, parcelas: int) -> dict:
    """Calcula parcela de financiamento pelo sistema Price."""
    taxa = taxa_mensal / 100
    if taxa == 0:
        parcela = valor / parcelas
    else:
        parcela = valor * (taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1)
    total_pago = parcela * parcelas
    total_juros = total_pago - valor
    return {
        "valor_financiado": valor,
        "taxa_mensal": taxa_mensal,
        "parcelas": parcelas,
        "valor_parcela": round(parcela, 2),
        "total_pago": round(total_pago, 2),
        "total_juros": round(total_juros, 2),
    }


def calcular_reserva_emergencia(renda_mensal: float, meses: int = 6) -> dict:
    """Calcula o valor ideal para reserva de emergência."""
    reserva = renda_mensal * meses
    return {
        "renda_mensal": renda_mensal,
        "meses_recomendados": meses,
        "reserva_ideal": round(reserva, 2),
        "economizar_por_mes_6meses": round(reserva / 6, 2),
        "economizar_por_mes_12meses": round(reserva / 12, 2),
    }


# ──────────────────────────────────────────────
# FAQ FINANCEIRO
# ──────────────────────────────────────────────

FAQ = {
    "poupança": "A poupança rende 0,5% ao mês + TR quando a Selic está acima de 8,5% ao ano. É segura (garantida pelo FGC até R$250 mil) mas costuma render abaixo da inflação.",
    "cdb": "O CDB (Certificado de Depósito Bancário) é um investimento de renda fixa emitido por bancos. Rende geralmente um percentual do CDI. Também é garantido pelo FGC até R$250 mil.",
    "tesouro direto": "O Tesouro Direto é um programa do governo federal para venda de títulos públicos a pessoas físicas. É considerado o investimento mais seguro do Brasil.",
    "selic": "A taxa Selic é a taxa básica de juros da economia brasileira, definida pelo COPOM a cada 45 dias. Ela influencia todos os outros juros do país.",
    "cdi": "O CDI (Certificado de Depósito Interbancário) é uma taxa usada entre bancos. Anda muito próximo da Selic e serve como referência para vários investimentos.",
    "fgc": "O FGC (Fundo Garantidor de Créditos) garante depósitos e investimentos em bancos de até R$250 mil por CPF por instituição, em caso de falência do banco.",
}


# ──────────────────────────────────────────────
# ASSISTENTE PRINCIPAL
# ──────────────────────────────────────────────

class AssistenteFinanceiro:
    def __init__(self):
        self.historico: list[dict] = []
        self.nome_usuario: str | None = None
        self.sessao_inicio = datetime.now().strftime("%d/%m/%Y %H:%M")

    def _detectar_calculo(self, mensagem: str) -> str | None:
        """Detecta se o usuário quer um cálculo financeiro e o executa."""
        msg = mensagem.lower()

        # Juros compostos
        if any(k in msg for k in ["juros compostos", "rendimento", "quanto vou ter"]):
            try:
                nums = [float(s.replace(",", ".")) for s in msg.split() if s.replace(",", ".").replace(".", "").isdigit()]
                if len(nums) >= 3:
                    res = calcular_juros_compostos(nums[0], nums[1], int(nums[2]))
                    return (
                        f"📊 **Simulação de Juros Compostos**\n"
                        f"• Capital inicial: R$ {res['principal']:,.2f}\n"
                        f"• Taxa mensal: {res['taxa_mensal']}%\n"
                        f"• Período: {res['meses']} meses\n"
                        f"• **Montante final: R$ {res['montante_final']:,.2f}**\n"
                        f"• Juros ganhos: R$ {res['juros_total']:,.2f} (+{res['rendimento_percentual']}%)"
                    )
            except Exception:
                pass

        # Financiamento
        if any(k in msg for k in ["financiamento", "parcela", "prestação"]):
            try:
                nums = [float(s.replace(",", ".")) for s in msg.split() if s.replace(",", ".").replace(".", "").isdigit()]
                if len(nums) >= 3:
                    res = calcular_parcela_financiamento(nums[0], nums[1], int(nums[2]))
                    return (
                        f"🏦 **Simulação de Financiamento (Tabela Price)**\n"
                        f"• Valor financiado: R$ {res['valor_financiado']:,.2f}\n"
                        f"• Taxa mensal: {res['taxa_mensal']}%\n"
                        f"• Parcelas: {res['parcelas']}x\n"
                        f"• **Valor da parcela: R$ {res['valor_parcela']:,.2f}**\n"
                        f"• Total a pagar: R$ {res['total_pago']:,.2f}\n"
                        f"• Total de juros: R$ {res['total_juros']:,.2f}"
                    )
            except Exception:
                pass

        # Reserva de emergência
        if any(k in msg for k in ["reserva de emergência", "emergência", "reserva"]):
            try:
                nums = [float(s.replace(",", ".")) for s in msg.split() if s.replace(",", ".").replace(".", "").isdigit()]
                if nums:
                    res = calcular_reserva_emergencia(nums[0])
                    return (
                        f"🛡️ **Reserva de Emergência Ideal**\n"
                        f"• Sua renda mensal: R$ {res['renda_mensal']:,.2f}\n"
                        f"• Reserva recomendada (6 meses): **R$ {res['reserva_ideal']:,.2f}**\n"
                        f"• Para atingir em 6 meses: R$ {res['economizar_por_mes_6meses']:,.2f}/mês\n"
                        f"• Para atingir em 12 meses: R$ {res['economizar_por_mes_12meses']:,.2f}/mês"
                    )
            except Exception:
                pass

        return None

    def conversar(self, mensagem_usuario: str) -> str:
        """Processa a mensagem e retorna a resposta da IA."""

        # Captura nome do usuário
        if not self.nome_usuario:
            for word in ["me chamo", "meu nome é", "sou o", "sou a"]:
                if word in mensagem_usuario.lower():
                    parts = mensagem_usuario.lower().split(word)
                    if len(parts) > 1:
                        self.nome_usuario = parts[1].strip().split()[0].capitalize()

        # Verifica se é um cálculo direto
        calculo = self._detectar_calculo(mensagem_usuario)
        if calculo:
            self.historico.append({"role": "user", "content": mensagem_usuario})
            self.historico.append({"role": "assistant", "content": calculo})
            return calculo

        # Consulta o modelo de IA
        self.historico.append({"role": "user", "content": mensagem_usuario})

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        if self.nome_usuario:
            messages[0]["content"] += f"\n\nO nome do usuário é {self.nome_usuario}. Use o nome para personalizar as respostas."

        messages.extend(self.historico[-10:])  # Mantém as últimas 10 mensagens (persistência de contexto)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=800,
            temperature=0.7,
        )

        resposta = response.choices[0].message.content.strip()
        self.historico.append({"role": "assistant", "content": resposta})
        return resposta

    def salvar_historico(self, arquivo: str = "historico_conversa.json") -> None:
        """Salva o histórico da conversa em JSON."""
        dados = {
            "sessao": self.sessao_inicio,
            "usuario": self.nome_usuario or "Anônimo",
            "mensagens": self.historico,
        }
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"\n💾 Histórico salvo em '{arquivo}'")


# ──────────────────────────────────────────────
# INTERFACE DE LINHA DE COMANDO
# ──────────────────────────────────────────────

def main():
    print("\n" + "═" * 58)
    print("  💰  FIN — Assistente Financeira Virtual com IA")
    print("  Desafio DIO · Thayná Batista da Silva · Senac Recife")
    print("═" * 58)
    print("  Digite 'sair' para encerrar · 'historico' para salvar")
    print("═" * 58 + "\n")

    assistente = AssistenteFinanceiro()

    # Mensagem de boas-vindas
    boas_vindas = assistente.conversar("Olá! Me apresente e diga como pode me ajudar com finanças.")
    print(f"🤖 FIN: {boas_vindas}\n")

    while True:
        try:
            entrada = input("Você: ").strip()
            if not entrada:
                continue
            if entrada.lower() in ["sair", "exit", "quit", "encerrar"]:
                print("\n🤖 FIN: Até logo! Boas finanças para você! 💚")
                break
            if entrada.lower() == "historico":
                assistente.salvar_historico()
                continue

            resposta = assistente.conversar(entrada)
            print(f"\n🤖 FIN: {resposta}\n")

        except KeyboardInterrupt:
            print("\n\n👋 Sessão encerrada.")
            break
        except Exception as e:
            print(f"\n❌ Erro: {e}\n")


if __name__ == "__main__":
    main()
