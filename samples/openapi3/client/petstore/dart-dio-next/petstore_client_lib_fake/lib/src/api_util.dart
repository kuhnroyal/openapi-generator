//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//

import 'dart:convert';
import 'dart:typed_data';

import 'package:built_collection/built_collection.dart';
import 'package:built_value/serializer.dart';
import 'package:dio/dio.dart';
import 'package:dio/src/parameter.dart';

/// Format the given form parameter object into something that Dio can handle.
/// Returns primitive or String.
/// Returns List/Map if the value is BuildList/BuiltMap.
Object? encodeFormParameter(Serializers serializers, Object? value, FullType type) {
  if (value == null) {
    return '';
  }
  if (value is String || value is num || value is bool) {
    return value;
  }
  final serialized = serializers.serialize(
    value as Object,
    specifiedType: type,
  );
  if (serialized is String) {
    return serialized;
  }
  if (value is BuiltList || value is BuiltSet || value is BuiltMap) {
    return serialized;
  }
  return json.encode(serialized);
}

Object? encodeQueryParameter(
  Serializers serializers,
  Object? value,
  FullType type,
) {
  if (value == null) {
    return '';
  }
  if (value is String || value is num || value is bool) {
    return value;
  }
  if (value is Uint8List) {
    // Currently not sure how to serialize this
    return value;
  }
  final serialized = serializers.serialize(
    value as Object,
    specifiedType: type,
  );
  if (serialized == null) {
    return '';
  }
  return serialized;
}

Object? encodeCollectionQueryParameter<T>(
  Serializers serializers,
  Object? value,
  FullType type, {
  ListFormat format = ListFormat.multi,
}) {
  if (!(value is BuiltList || value is BuiltSet || value is BuiltMap)) {
    throw ArgumentError('Invalid non-collection value passed to encodeCollectionQueryParameter');
  }
  final serialized = serializers.serialize(
    value as Object,
    specifiedType: type,
  );
  if (value is BuiltList || value is BuiltSet) {
    return ListParam<T>(List.of((serialized as Iterable<Object?>).cast()), format);
  }
  // Return the serialized value, this can only be a map at this point
  return serialized;
}
