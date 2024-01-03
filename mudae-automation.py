from seleniumbase import SB

def verify_success(sb):
    sb.sleep(1)

def perform_login(sb):
    # Clique no botão de login (ajuste o seletor conforme necessário)
    sb.click('#__next > div > div > div.page__PageContentWrapper-sc-iv577v-0.bKsFTH > div.chakra-stack.chakra-container.css-12w0nwo > div > div > div.chakra-stack.css-iqiv3e > div.chakra-stack.css-qffgy4 > div.css-u6mj1a > div > a')

    sb.sleep(20)
    # Preencha os campos de email e senha
    sb.type('#uid_6', "seu-email")  # Ajuste o seletor do campo de email
    sb.type("#uid_8", "sua-senha")  # Ajuste o seletor do campo de senha

    # Submeta o formulário de login
    sb.click('#app-mount > div.appAsidePanelWrapper__714a6 > div.notAppAsidePanel__9d124 > div.app_b1f720 > div > div > div > div > form > div.centeringWrapper__319b0 > div > div.mainLoginContainer__58502 > div.block__8bc50.marginTop20_d88ee7 > button.marginBottom8_f4aae3.button__47891.button_afdfd9.lookFilled__19298.colorBrand_b2253e.sizeLarge__9049d.fullWidth__7c3e8.grow__4c8a4')  # Ajuste o seletor do botão de submissão

    sb.sleep(10)

    sb.click('#app-mount > div.appAsidePanelWrapper__714a6 > div.notAppAsidePanel__9d124 > div.app_b1f720 > div > div > div > div > div > div.footer__04ee2 > button.button_afdfd9.lookFilled__19298.colorBrand_b2253e.sizeMedium_c6fa98.grow__4c8a4')

    sb.sleep(25)

    #Vote button

    sb.click("button:contains('Vote')")

    sb.sleep(10)



with SB(uc_cdp=True) as sb:
    sb.open("https://top.gg/bot/432610292342587392/vote")
    try:
        verify_success(sb)
    except Exception:
        sb.sleep(5)
        if sb.is_element_visible('input[value*="Verify"]'):
            sb.click('input[value*="Verify"]')
        elif sb.is_element_visible('iframe[title*="challenge"]'):
            sb.switch_to_frame('iframe[title*="challenge"]')
            sb.click("span.mark")
        else:
            raise Exception("Detected!")

        # Tente verificar novamente após clicar no desafio
        try:
            verify_success(sb)
        except Exception:
            raise Exception("Detected!")

    # Realiza o processo de login
    perform_login(sb)
