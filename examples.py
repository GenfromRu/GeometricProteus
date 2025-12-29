"""
examples.py - Примеры использования Geometric Proteus
Автор: [Ваше Имя]
Дата: [Дата]
"""

from geometric_proteus import GeometricProteus

def example_basic_usage():
    """Базовый пример использования."""
    print("1. БАЗОВОЕ ИСПОЛЬЗОВАНИЕ:")
    print("-" * 40)
    
    proteus = GeometricProteus()
    
    # Шифрование
    encrypted = proteus.encrypt("Привет, мир!", "мой_секрет")
    print(f"Зашифровано: {encrypted['data'][:50]}...")
    
    # Расшифровка
    decrypted = proteus.decrypt(encrypted, "мой_секрет")
    print(f"Расшифровано: {decrypted}")

def example_performance_test():
    """Тест производительности."""
    print("\n2. ТЕСТ ПРОИЗВОДИТЕЛЬНОСТИ:")
    print("-" * 40)
    
    proteus = GeometricProteus()
    
    # Тест на разных размерах
    for size in [1000, 10000, 50000]:
        print(f"\nРазмер: {size:,} байт")
        proteus.benchmark(size)

def example_np_proof():
    """Демонстрация NP-трудности."""
    print("\n3. ДЕМОНСТРАЦИЯ NP-ТРУДНОСТИ:")
    print("-" * 40)
    
    from geometric_proteus import NPComplexityProver
    NPComplexityProver.prove_np_hardness()

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ GEOMETRIC PROTЕUS")
    print("=" * 60)
    
    example_basic_usage()
    example_performance_test()
    example_np_proof()
    
    print("\n" + "=" * 60)
    print("✅ Все примеры выполнены успешно!")