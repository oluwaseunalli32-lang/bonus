import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋 Sou um bot educacional sobre Inteligência Artificial.\n"
        "Use /dica para receber uma dica sobre IA.\n"
        "Use /privacidade para ver a política de privacidade.\n"
        "Use /apagar para solicitar a exclusão dos seus dados."
    )

async def dica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Dica de IA: Modelos de linguagem aprendem padrões a partir de grandes volumes de texto."
    )

async def privacidade(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Política de Privacidade: este bot não coleta dados pessoais. "
        "Nenhuma informação é armazenada. Para dúvidas, contate o administrador."
    )

async def apagar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Seus dados não são armazenados, portanto não há nada a excluir. "
        "Se você acredita que algum dado foi coletado, contate o administrador."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("dica", dica))
    app.add_handler(CommandHandler("privacidade", privacidade))
    app.add_handler(CommandHandler("apagar", apagar))
    app.run_polling()
