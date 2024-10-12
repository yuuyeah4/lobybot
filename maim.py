import fortnitepy

client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
app_id = "YOUR_APP_ID"

# ログインとボットの処理をここに記述
client = fortnitepy.Client(
    auth=fortnitepy.AdvancedAuth(
        client_id=client_id,
        client_secret=client_secret,
        launcher_token="eg1",
        game_token="eg1",
        app_id=app_id
    )
)

@client.event
async def event_ready():
    print(f"Bot is ready as {client.user.display_name}")

client.run()
