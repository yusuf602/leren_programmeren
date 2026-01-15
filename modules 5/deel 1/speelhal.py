from help import *
RECEIPT_TEXT = '***** SPEELHAL ENTREE VOOR {personen:2} PERSONEN *****'
RESTART_TEXT = '\nBestelprocedure gestopt door invoerfout!\nHerstart de bestelprocedure!'
MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5
TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89
VAT_CODE_H = 'H'
VAT_CODE_L = 'L'

print("SPEELHAL-ENTREE-KASSA")
answer = input_yes_no("Wilt u bestellen?(j/n)") 

if answer.lower() in ('j','ja'):
  print('Ik ga u nu vragen wat en hoeveel u wilt...')

else:
  exit('Nu geen interesse? Tot ziens!')

nr_tickets = input_int(f"Hoeveel personen? (min 1, max {MAX_TICKETS}) ", 1, MAX_TICKETS)

answer = input_yes_no (" Ook VR-VIP seats? (j/n) ")

vr_vip_ordered = answer.lower == 'j' 'J'

if vr_vip_ordered:
  nr_vr_vip_seats = input_int(f"hoeveel VR-VIP seats? (0 t/m {nr_tickets}) ", 0, nr_tickets)
  vr_vip_seat_time = input_int(f"hoeveel minuten in de VR-VIP-seats? (5 t/m {MAX_VR_VIP_SEAT_TIME})",5, MAX_VR_VIP_SEAT_TIME)

nr_cola = input_int(f"Hoeveel cola? (0 t/m {nr_tickets})",0, nr_tickets) 
nr_popcorn = input_int(f"Hoeveel popcorn? (0 t/m {nr_tickets})" , 0,  nr_tickets)
if input_yes_no ("Wilt u een factuur met BTW specificatie?(J/N)"):
    print("U koos voor een factuur met BTW specificatie.")
else:
    print("U koos voor een factuur zonder BTW specificatie.")

vat_invoice = answer in ('j''J')
if vat_invoice:
  company_name = input("Op welke bedrijfsnaam komt de factuur?").strip or "........... (zelf invullen)"

total_tickets = round(nr_tickets * TICKET_PRICE,2)
vr_vip_seat_price = vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE
total_vr_vip_seats = round(nr_vr_vip_seats * vr_vip_seat_price, 2)
total_cola = round(nr_cola * COLA_PRICE, 2)
total_popcorn = round(nr_popcorn * POPCORN_PRICE, 2)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

if vat_invoice:
    total_tickets_vat = get_vat_from_amount_incl(total_tickets, 'H')
    total_vr_vip_seats_vat = get_vat_from_amount_incl(total_vr_vip_seats, 'H')

    total_cola_ex_vat = get_vat_from_amount_incl(total_cola, 'L')
    total_popcorn_ex_vat = get_vat_from_amount_incl(total_popcorn, 'L')

    total_vat_H = total_tickets_vat + total_vr_vip_seats_vat
    total_vat_L = total_cola_ex_vat + total_popcorn_ex_vat
    total_vat = total_vat_H + total_vat_L

receipt_text = RECEIPT_TEXT.format(personen = nr_tickets)
print(receipt_text+'\n')
if vat_invoice:
  print(f'Factuur voor: {company_name}')
else:
  print(f'Kassabon')\
  
print('-'*len(receipt_text))
print(f'Tickets                   {nr_tickets:2} x {TICKET_PRICE:2.2f} = {total_tickets:6.2f}')
print(f'VR-vip-seats  {vr_vip_seat_time:3} minuten {nr_vr_vip_seats:2} x {vr_vip_seat_price:2.2f} = {total_vr_vip_seats:6.2f}')
print(f'Cola                      {nr_cola:2} x {COLA_PRICE:2.2f} = {total_cola:6.2f}')
print(f'Popcorn                   {nr_popcorn:2} x {POPCORN_PRICE:2.2f} = {total_popcorn:6.2f}')
print('.'*len(receipt_text))
print(f'Totaal:                               {total_all:6.2f}')

print()
if vat_invoice:
    vat_perc_H = get_vat_perc(VAT_CODE_H)
    vat_perc_L = get_vat_perc(VAT_CODE_L)

    print(f'BTW Hoog                          {vat_perc_H:2}% {total_vat_H:6.2f}')
    print(f'BTW Laag                          {vat_perc_L:2}% {total_vat_L:6.2f}')

print('=' * len(receipt_text))
print('Bedankt voor de bestelling, veel plezier!')