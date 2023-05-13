import 'package:test/test.dart';
import 'package:openapi/openapi.dart';

// tests for MapTest
void main() {
  final instance = MapTestBuilder();
  // add properties to the builder and call build()

  group(MapTest, () {
    // BuiltMap<String, BuiltMap<String, String>> mapMapOfString
    test('to test the property `mapMapOfString`', () async {});

    // BuiltMap<String, String> mapOfEnumString
    test('to test the property `mapOfEnumString`', () async {});

    // BuiltMap<String, bool> directMap
    test('to test the property `directMap`', () async {});

    // BuiltMap<String, bool> indirectMap
    test('to test the property `indirectMap`', () async {});
  });
}
