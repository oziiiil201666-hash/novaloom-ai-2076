import 'dart:convert';
import 'package:http/http.dart' as http;

class RailwayService {
  final String baseUrl;
  RailwayService({this.baseUrl = 'https://YOUR-RAILWAY-APP.up.railway.app'});

  Future<dynamic> getDashboard() async {
    final res = await http.get(Uri.parse('$baseUrl/enterprise/dashboard'));
    if (res.statusCode == 200) return jsonDecode(res.body);
    throw Exception('Dashboard error: ${res.statusCode}');
  }

  Future<dynamic> getDesigns({String sortBy = 'newest'}) async {
    final res = await http.get(Uri.parse('$baseUrl/ai/designs?sort_by=$sortBy'));
    if (res.statusCode == 200) return jsonDecode(res.body);
    throw Exception('Designs error: ${res.statusCode}');
  }

  Future<dynamic> getInventory() async {
    final res = await http.get(Uri.parse('$baseUrl/enterprise/inventory'));
    if (res.statusCode == 200) return jsonDecode(res.body);
    throw Exception('Inventory error: ${res.statusCode}');
  }
}
