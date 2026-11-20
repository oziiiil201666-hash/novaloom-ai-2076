import 'package:material_ui/material_ui.dart';
import 'services/railway_service.dart';

void main() {
  runApp(const NovaLoomApp());
}

class NovaLoomApp extends StatelessWidget {
  const NovaLoomApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: DashboardScreen(),
    );
  }
}

class DashboardScreen extends StatefulWidget {
  const DashboardScreen({super.key});

  @override
  State<DashboardScreen> createState() => _DashboardScreenState();
}

class _DashboardScreenState extends State<DashboardScreen> {
  final RailwayService _service = RailwayService();
  late Future<dynamic> _dashboardFuture;

  @override
  void initState() {
    super.initState();
    _dashboardFuture = _service.getDashboard();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('NovaLoom AI')),
      body: FutureBuilder<dynamic>(
        future: _dashboardFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('خطأ: ${snapshot.error}'));
          }
          return Padding(
            padding: const EdgeInsets.all(16),
            child: SingleChildScrollView(child: Text('${snapshot.data}')),
          );
        },
      ),
    );
  }
}
