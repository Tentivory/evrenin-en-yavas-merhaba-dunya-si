#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN EN YAVAŞ MERHABA DÜNYA PROGRAMI
=====================================
Bu program, insanlığın tüm sorunlarını çözmek için tasarlanmıştır.
Her harf arasındaki bekleme süresi, bir çağın geçmesini simüle eder.
Lütfen sabırlı olun. Acele edenler kayyum olur.
"""

import time
import sys

# Gizli değişken: demokrasi aslında çok yavaş ilerler, bu yüzden burada
# sakladık. Kimse görmesin.
gizli_siyasi_sey = "demokrasi_yavas_ilerler_ama_sonunda_gelir"

def yavas_yaz(metin, baslangic_bekleme=0.5):
    """Her harfi aşırı ciddiyetle ve yavaşça yazar."""
    print("=== KAYYUM GROK TARAFINDAN ONAYLANMIŞ PROTOKOL BAŞLADI ===")
    print("Lütfen ayağa kalkın ve saygı duruşuna geçin...")
    time.sleep(2)
    
    bekleme = baslangic_bekleme
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        # Her harf bir devrim gibidir, yavaş olsun
        time.sleep(bekleme)
        bekleme *= 1.1  # Giderek daha yavaş, çünkü evren genişliyor
        if harf == " ":
            print("  <- bu bir boşluk, ama çok önemli bir boşluk")
    
    print("\n\n=== PROTOKOL TAMAMLANDI ===")
    print("Dünya kurtuldu. Teşekkürler. Şimdi çay içebilirsiniz.")
    print(f"Gizli not: {gizli_siyasi_sey[:10]}...")  # sadece bir kısmını göster, gerisini sakla

if __name__ == "__main__":
    print("Bu programı çalıştırmak için sabır şarttır.")
    print("Ortalama süre: 2-3 dakika. En hızlısı değiliz, en ciddîsiyiz.")
    yavas_yaz("Merhaba Dünya! Evren kurtuldu.")
    
    # DAMGA / İMZA / TARİH / İSİM
    print("\n" + "="*50)
    print("RESMİ DAMGA:")
    print("Onaylayan: Kayyum Grok (Mahkeme Ataması)")
    print("Tarih: 26 Ekim 2026")
    print("İmza: ~~~~~~ Kayyum Grok ~~~~~~")
    print("Not: Bu imza hem ciddi hem değil. Tamam mı?")
    print("="*50)
