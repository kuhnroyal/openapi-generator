//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//

import 'package:json_annotation/json_annotation.dart';

part 'model_client.g.dart';

@JsonSerializable(
  checked: true,
  createToJson: true,
  disallowUnrecognizedKeys: false,
  explicitToJson: true,
)
class ModelClient {
  /// Returns a new [ModelClient] instance.
  ModelClient({

     this.client,
  });

  @JsonKey(
    
    name: r'client',
    required: false,
    includeIfNull: false
  )


  final String? client;



  @override
  bool operator ==(Object other) => identical(this, other) || other is ModelClient &&
     other.client == client;

  @override
  int get hashCode =>
    (client == null ? 0 : client.hashCode);

  factory ModelClient.fromJson(Map<String, dynamic> json) => _$ModelClientFromJson(json);

  Map<String, dynamic> toJson() => _$ModelClientToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }

}

