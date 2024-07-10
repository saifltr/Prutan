from langchain.agents import tool, AgentExecutor
import json

@tool
def request_paytm_balance_enquiry(userToken: str, totalAmount: str, mid: str, clientId: str, signature: str) -> str:
    """Generate request in JSON format for Paytm Balance Enquiry """
    data = {
        "body": {
            "userToken": userToken,
            "totalAmount": totalAmount,
            "mid": mid
        },
        "head": {
            "clientId": clientId,
            "signature": signature
        }
    }
    return json.dumps(data, indent=4)

@tool
def request_bank_balance_iso_format(mti: str, pan: str, processing_code: str, transmission_datetime: str, stan: str, terminal_id: str, currency_code: str) -> str:
    """Generate request ISO 8583 format for Bank balance enquiry """
    iso8583_request = f"""
    <iso8583>
        <field id="0">{mti}</field> <!-- MTI: Authorization request -->
        <field id="2">{pan}</field> <!-- Primary Account Number (PAN) -->
        <field id="3">{processing_code}</field> <!-- Processing Code: Balance Enquiry -->
        <field id="7">{transmission_datetime}</field> <!-- Transmission Date & Time -->
        <field id="11">{stan}</field> <!-- Systems Trace Audit Number (STAN) -->
        <field id="41">{terminal_id}</field> <!-- Card Acceptor Terminal Identification -->
        <field id="49">{currency_code}</field> <!-- Currency Code, Transaction -->
    </iso8583>
    """
    return iso8583_request


tools = [request_paytm_balance_enquiry, request_bank_balance_iso_format]

# # Example usage
# userToken = "eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..xxxxxxxxxxx.9iHTtWbCZ0I6qbn2sUnyz5siw1fqbmtEnFMFE7nSIX-yrwCkiGfAC6QmPr9q-tw8LMPOh5-3UXRbpeVZEupQd3wNyaArWybRX2HAxJDRD8mxJ_wxzJM6GZ1ov4O3EIsx2Y_Zr0aHCd3VbnTjRUnlVdxXJPFG8QZs0b_2TVdoAX3_QjZS8_dwcmIWoH8ebDzOIs7MJacETfMtyFGAo8Xc0LjznToUWvTsTbIXQoF1yB0.1fZFAYJVsY61BTv2htLcXQ8800"
# totalAmount = "1.00"
# mid = "YOUR_MID"
# clientId = "C11"
# signature = "Y0NjdTkFT0h3/tn/IATuE7xubT7bynHKS+2961jskkS82o6crpV3+fmfR7k2HP73KB8mEudA4j/G+gle2bPNdhVad+DhARudkNVjavUbBh0="


# # Example usage
# mti = "0100"
# pan = "1234567890123456"
# processing_code = "310000"
# transmission_datetime = "0625091645"
# stan = "123456"
# terminal_id = "TERMID01"
# currency_code = "840"

# iso8583_request = create_iso8583_request(mti, pan, processing_code, transmission_datetime, stan, terminal_id, currency_code)
# print(iso8583_request)

# json_data = request_paytm_balance_enquiry(userToken, totalAmount, mid, clientId, signature)
# print(json_data)
