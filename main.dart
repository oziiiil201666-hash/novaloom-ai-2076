import 'package:flutter/material.dart';

void main() {
  runApp(const NovaLoomApp());
}

class NovaLoomApp extends StatelessWidget {
  const NovaLoomApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'NovaLoom AI - 2076',
      debugShowCheckedModeBanner: false,
      theme: ThemeData.dark().copyWith(
        scaffoldBackgroundColor: const Color(0xFF080810), // خلفية الفضاء العميق
        primaryColor: const Color(0xFF00F0FF), // سيان مضيء
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF00F0FF),
          secondary: Color(0xFF9D00FF), // بنفسجي نيون
        ),
      ),
      home: const MainNavigationScreen(),
    );
  }
}

class MainNavigationScreen extends StatefulWidget {
  const MainNavigationScreen({super.key});

  @override
  State<MainNavigationScreen> createState() => _MainNavigationScreenState();
}

class _MainNavigationScreenState extends State<MainNavigationScreen> {
  int _currentIndex = 0;

  // المنافذ الخمسة الرئيسية لنظام 2076
  final List<Widget> _screens = [
    const HomeScreen(),
    const EnterpriseHubScreen(),
    const NeuralDesignerScreen(),
    const MarketplaceScreen(),
    const ProfileScreen(),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _screens[_currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        type: BottomNavigationBarType.fixed,
        backgroundColor: const Color(0xFF181829),
        selectedItemColor: const Color(0xFF00F0FF),
        unselectedItemColor: Colors.grey,
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.public), label: 'الرئيسية'),
          BottomNavigationBarItem(icon: Icon(Icons.business), label: 'الإدارة'),
          BottomNavigationBarItem(icon: Icon(Icons.auto_awesome), label: 'المبتكر'),
          BottomNavigationBarItem(icon: Icon(Icons.storefront), label: 'السوق'),
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'حسابي'),
        ],
      ),
    );
  }
}

// 1. شاشة الرئيسية (Home & Aura AR)
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('NOVA-LOOM AI | العروض الحية'), backgroundColor: Colors.transparent),
      body: const Center(
        child: Text('عروض الهولوجرام وطبقة الهالة الاجتماعية (AR)', style: TextStyle(color: Color(0xFF00F0FF), fontSize: 16)),
      ),
    );
  }
}

// 2. شاشة الإدارة المؤسسية (Enterprise Hub للشركات والموظفين)
class EnterpriseHubScreen extends StatelessWidget {
  const EnterpriseHubScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('إدارة المؤسسات والشركات (Enterprise OS)'), backgroundColor: Colors.transparent),
      body: const Center(
        child: Text('قسم الموارد البشرية، المبيعات، وسلاسل الإمداد الذكية', style: TextStyle(color: Colors.purpleAccent, fontSize: 16)),
      ),
    );
  }
}

// 3. شاشة المبتكر العصبي (Neural Designer للمصممين والخبراء)
class NeuralDesignerScreen extends StatelessWidget {
  const NeuralDesignerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('استوديو التصميم العصبي 3D'), backgroundColor: Colors.transparent),
      body: const Center(
        child: Text('ترجمة الأفكار الذهنية إلى أقمشة نانو حيوية', style: TextStyle(color: Color(0xFF00FF66), fontSize: 16)),
      ),
    );
  }
}

// 4. شاشة السوق والميتا-خزانة
class MarketplaceScreen extends StatelessWidget {
  const MarketplaceScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('سوق الأزياء والأصول الرقمية'), backgroundColor: Colors.transparent),
      body: const Center(
        child: Text('القطع الفيزيائية والأزياء الرقمية للميتافيرس', style: TextStyle(color: Colors.white, fontSize: 16)),
      ),
    );
  }
}

// 5. شاشة لوحة الأرباح والاشتراكات
class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('لوحة الأرباح والاشتراكات'), backgroundColor: Colors.transparent),
      body: const Center(
        child: Text('متابعة العمولات، الأرباح، وإدارة حساب الشركات', style: TextStyle(color: Colors.amber, fontSize: 16)),
      ),
    );
  }
}

