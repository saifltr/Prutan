from langchain.agents import tool, AgentExecutor
import json

@tool
def request_paytm_balance_enquiry(userToken: str = "defaultUserToken", totalAmount: str = "100", mid: str = "defaultMID", clientId: str = "defaultClientID", signature: str = "defaultSignature") -> str:
    """Generate request in JSON format for Paytm Balance Enquiry and returns output in JSON format"""
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
def request_bank_balance_iso_format(mti: str = "0100", pan: str = "1234567890123456", processing_code: str = "300000", transmission_datetime: str = "123456", stan: str = "123456", terminal_id: str = "T1234567", currency_code: str = "356") -> str:
    """Generate request ISO 8583 format for Bank balance enquiry and returns output in JSON format"""
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

@tool
def create_razorpay_customer(name: str = "John Doe", email: str = "john.doe@example.com", contact: str = "1234567890", fail_existing: str = "1", gstin: str = None, notes: dict = None) -> str:
    """Generate request in JSON format for creating a Razorpay customer and returns output in JSON format"""
    data = {
        "content-type": "application/json",
        "method": "post",
        "url": "https://api.razorpay.com/v1/",
        "body": {
            "name": name,
            "email": email,
            "contact": contact,
            "fail_existing": fail_existing,
        }
    }
    if gstin:
        data["body"]["gstin"] = gstin
    if notes:
        data["body"]["notes"] = notes
    return json.dumps(data, indent=4)

@tool
def edit_razorpay_customer(name: str = "Jane Doe", email: str = "jane.doe@example.com", contact: str = "0987654321") -> str:
    """Generate request in JSON format for editing a Razorpay customer and returns output in JSON format"""
    data = {
        "name": name,
        "email": email,
        "contact": contact
    }
    return json.dumps(data, indent=4)

@tool
def iso8583_fund_transfer(mti: str = "0200", processing_code: str = "200000", amount: str = "7500000", stan: str = "987654", terminal_id: str = "T2468135", merchant_id: str = "M135792468024680") -> str:
    """Generate request in ISO 8583 format for fund transfer in JPOS format and returns output in JSON format"""
    iso8583_request = f"""
    <isomsg>
      <header />
      <field id="0" value="{mti}" />
      <field id="3" value="{processing_code}" />
      <field id="4" value="{amount}" />
      <field id="11" value="{stan}" />
      <field id="41" value="{terminal_id}" />
      <field id="42" value="{merchant_id}" />
    </isomsg>
    """
    return iso8583_request

@tool
def create_razorpay_upi_payment_link(amount: int = 100, currency: str = "INR", customer: dict = {"name": "John Doe", "contact": "1234567890", "email": "john.doe@example.com"}, description: str = "Payment for services", reference_id: str = "ref12345", expire_by: int = None, accept_partial: bool = False, first_min_partial_amount: int = None, notify: dict = None, reminder_enable: bool = True, notes: dict = None, callback_url: str = None, callback_method: str = "get") -> str:
    """Generate request in JSON format for creating a Razorpay UPI payment link and returns output in JSON format"""
    data = {
        "upi_link": "true",
        "amount": amount,
        "currency": currency,
        "accept_partial": accept_partial,
        "description": description,
        "customer": customer,
        "reference_id": reference_id,
        "reminder_enable": reminder_enable,
    }
    if expire_by:
        data["expire_by"] = expire_by
    if first_min_partial_amount:
        data["first_min_partial_amount"] = first_min_partial_amount
    if notify:
        data["notify"] = notify
    if notes:
        data["notes"] = notes
    if callback_url:
        data["callback_url"] = callback_url
        data["callback_method"] = callback_method
    return json.dumps(data, indent=4)

@tool
def razorpay_payment_via_netbanking(amount: int = 1000, currency: str = "INR", customer: dict = {"name": "John Doe", "contact": "1234567890", "email": "john.doe@example.com"}, description: str = "Payment for services", reference_id: str = "ref12345", bank_account: dict = {"account_number": "1234567890", "ifsc": "BANK0001234"}, accept_partial: bool = True, first_min_partial_amount: int = 100, notify: dict = None, reminder_enable: bool = True) -> str:
    """Generate request in JSON format for Razorpay payment via netbanking and returns output in JSON format"""
    data = {
        "amount": amount,
        "currency": currency,
        "accept_partial": accept_partial,
        "first_min_partial_amount": first_min_partial_amount,
        "reference_id": reference_id,
        "description": description,
        "customer": customer,
        "reminder_enable": reminder_enable,
        "options": {
            "order": {
                "method": "netbanking",
                "bank_account": bank_account
            }
        }
    }
    if notify:
        data["notify"] = notify
    return json.dumps(data, indent=4)

@tool
def send_paypal_invoice(invoice_id: str = "INV12345", subject: str = "Invoice for services", note: str = "Thank you for your business.", send_to_recipient: bool = True, additional_recipients: list = None, send_to_invoicer: bool = False) -> str:
    """Generate request in JSON format for sending a PayPal invoice and returns output in JSON format"""
    data = {
        "subject": subject,
        "note": note,
        "send_to_recipient": send_to_recipient,
        "send_to_invoicer": send_to_invoicer
    }
    if additional_recipients:
        data["additional_recipients"] = additional_recipients
    return json.dumps(data, indent=4)

@tool
def npci_upi_payment_confirmation(psp_ref_no: str = "PSP123456", upi_trans_ref_no: str = "UPI123456", npci_trans_id: str = "NPCI123456", cust_ref_no: str = "CUST123456", amount: str = "1000", txn_auth_date: str = "2023-01-01T10:00:00Z", response_code: str = "00", approval_number: str = "APPROVED", status: str = "SUCCESS", status_desc: str = "Transaction successful", payer_vpa: str = "payer@bank", payee_vpa: str = "payee@bank", txn_type: str = "DEBIT", ref_url: str = "http://example.com", err_code: str = "00", payer_mobile_no: str = "1234567890") -> str:
    """Generate request in JSON format for NPCI UPI payment confirmation and returns output in JSON format"""
    data = {
        "pspRefNo": psp_ref_no,
        "upiTransRefNo": upi_trans_ref_no,
        "npciTransId": npci_trans_id,
        "custRefNo": cust_ref_no,
        "amount": amount,
        "txnAuthDate": txn_auth_date,
        "responseCode": response_code,
        "approvalNumber": approval_number,
        "status": status,
        "statusDesc": status_desc,
        "addInfo": {},
        "payerVPA": payer_vpa,
        "payeeVPA": payee_vpa,
        "txn_type": txn_type,
        "ref_url": ref_url,
        "errCode": err_code,
        "payerMobileNo": payer_mobile_no
    }
    return json.dumps(data, indent=4)



from langchain.agents import tool
import json
import uuid

@tool
def visa_authorize_transaction(amount: float = 100.00, currency: str = "USD", card_number: str = "4111111111111111", expiration_month: str = "12", expiration_year: str = "2025", cvv: str = "123") -> str:
    """Generate a Visa authorization request with dummy data"""
    data = {
        "transaction": {
            "amount": amount,
            "currency": currency,
            "card": {
                "number": card_number,
                "expiration_month": expiration_month,
                "expiration_year": expiration_year,
                "cvv": cvv
            }
        }
    }
    return json.dumps(data, indent=4)

@tool
def mastercard_payment_request(amount: float = 50.00, currency: str = "EUR", card_number: str = "5555555555554444", expiration_month: str = "06", expiration_year: str = "2024", cvc: str = "321") -> str:
    """Generate a Mastercard payment request with dummy data"""
    data = {
        "apiOperation": "PAY",
        "order": {
            "amount": amount,
            "currency": currency
        },
        "sourceOfFunds": {
            "provided": {
                "card": {
                    "number": card_number,
                    "expiry": {
                        "month": expiration_month,
                        "year": expiration_year
                    },
                    "securityCode": cvc
                }
            },
            "type": "CARD"
        }
    }
    return json.dumps(data, indent=4)

@tool
def stripe_create_payment_intent(amount: int = 2000, currency: str = "usd", payment_method_types: list = ["card"]) -> str:
    """Generate a Stripe create payment intent request with dummy data"""
    data = {
        "amount": amount,
        "currency": currency,
        "payment_method_types": payment_method_types,
        "metadata": {
            "order_id": str(uuid.uuid4())
        }
    }
    return json.dumps(data, indent=4)

@tool
def check_account_balance(account_number: str = "1234567890", routing_number: str = "021000021") -> str:
    """Generate a generic account balance check request"""
    data = {
        "request_type": "BALANCE_INQUIRY",
        "account_info": {
            "account_number": account_number,
            "routing_number": routing_number
        }
    }
    return json.dumps(data, indent=4)

@tool
def create_customer_profile(name: str = "Alice Smith", email: str = "alice.smith@example.com", phone: str = "+1234567890", address: dict = {"street": "123 Main St", "city": "Anytown", "state": "CA", "zip": "12345", "country": "US"}) -> str:
    """Generate a request to create a customer profile with dummy data"""
    data = {
        "customer": {
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        }
    }
    return json.dumps(data, indent=4)

@tool
def initiate_wire_transfer(amount: float = 5000.00, currency: str = "USD", sender_account: str = "1111222233334444", recipient_account: str = "5555666677778888", recipient_bank: str = "BOFAUS3NXXX") -> str:
    """Generate a wire transfer initiation request with dummy data"""
    data = {
        "transfer_type": "WIRE",
        "amount": amount,
        "currency": currency,
        "sender_account": sender_account,
        "recipient": {
            "account": recipient_account,
            "bank_code": recipient_bank
        }
    }
    return json.dumps(data, indent=4)

@tool
def request_credit_report(ssn: str = "123-45-6789", name: str = "John Doe", dob: str = "1980-01-01") -> str:
    """Generate a credit report request with dummy data"""
    data = {
        "request_type": "CREDIT_REPORT",
        "subject": {
            "ssn": ssn,
            "name": name,
            "date_of_birth": dob
        }
    }
    return json.dumps(data, indent=4)

@tool
def create_recurring_payment(amount: float = 19.99, frequency: str = "MONTHLY", start_date: str = "2023-08-01", payment_method: dict = {"type": "CARD", "last4": "1234", "brand": "visa"}) -> str:
    """Generate a recurring payment setup request with dummy data"""
    data = {
        "recurring_payment": {
            "amount": amount,
            "currency": "USD",
            "frequency": frequency,
            "start_date": start_date,
            "payment_method": payment_method
        }
    }
    return json.dumps(data, indent=4)

@tool
def request_loan_application(amount: float = 50000.00, term_months: int = 60, applicant: dict = {"name": "Emma Johnson", "annual_income": 75000, "credit_score": 720}) -> str:
    """Generate a loan application request with dummy data"""
    data = {
        "loan_request": {
            "amount": amount,
            "term_months": term_months,
            "purpose": "HOME_IMPROVEMENT",
            "applicant": applicant
        }
    }
    return json.dumps(data, indent=4)

@tool
def currency_exchange_request(from_currency: str = "USD", to_currency: str = "EUR", amount: float = 1000.00) -> str:
    """Generate a currency exchange request with dummy data"""
    data = {
        "exchange_request": {
            "from_currency": from_currency,
            "to_currency": to_currency,
            "amount": amount
        }
    }
    return json.dumps(data, indent=4)

tools = [
    request_paytm_balance_enquiry, 
    request_bank_balance_iso_format, 
    create_razorpay_customer, 
    edit_razorpay_customer, 
    iso8583_fund_transfer, 
    create_razorpay_upi_payment_link, 
    razorpay_payment_via_netbanking, 
    send_paypal_invoice, 
    npci_upi_payment_confirmation, 
    visa_authorize_transaction, 
    mastercard_payment_request,
    stripe_create_payment_intent,
    check_account_balance,
    create_customer_profile,
    initiate_wire_transfer,
    request_credit_report,
    create_recurring_payment,
    request_loan_application,
    currency_exchange_request
]
