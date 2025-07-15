from supabase import create_client, Client
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if SUPABASE_URL is None or SUPABASE_KEY is None:
    raise ValueError(
        "SUPABASE_URL and SUPABASE_KEY environment variables must be set")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_closed_trades():
    response = supabase.table('closed_trades').select('*').execute()
    return response.data


def get_transactions():
    response = supabase.table('transactions').select('*').execute()
    return response.data

def get_strategies():
    response = supabase.table('strategies').select('*').execute()
    return response.data


def get_open_trades():
    # Get all BUY transactions
    transactions = supabase.table('transactions').select(
        '*').eq('side', 'BUY').execute().data
    # Get all trades with a buy_order_id
    trades = supabase.table('closed_trades').select(
        'buy_order_id').execute().data
    # Create a set of buy_order_ids from trades
    buy_order_ids = set(trade['buy_order_id']
                        for trade in trades if trade['buy_order_id'] is not None)
    # Return BUY transactions whose order_id is not in buy_order_ids
    open_trades = [tx for tx in transactions if tx['order_id']
                   not in buy_order_ids]
    return open_trades


def get_balance():
    response = supabase.table('equity').select('*').execute()
    return response.data
