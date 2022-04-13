//
// AUTO-GENERATED FILE, DO NOT MODIFY!
//

import 'package:json_annotation/json_annotation.dart';

part 'outer_composite.g.dart';

@JsonSerializable(
  checked: true,
  createToJson: true,
  disallowUnrecognizedKeys: false,
  explicitToJson: true,
)
class OuterComposite {
  /// Returns a new [OuterComposite] instance.
  OuterComposite({

     this.myNumber,

     this.myString,

     this.myBoolean,
  });

  @JsonKey(
    
    name: r'my_number',
    required: false,
    includeIfNull: false
  )


  final num? myNumber;



  @JsonKey(
    
    name: r'my_string',
    required: false,
    includeIfNull: false
  )


  final String? myString;



  @JsonKey(
    
    name: r'my_boolean',
    required: false,
    includeIfNull: false
  )


  final bool? myBoolean;



  @override
  bool operator ==(Object other) => identical(this, other) || other is OuterComposite &&
     other.myNumber == myNumber &&
     other.myString == myString &&
     other.myBoolean == myBoolean;

  @override
  int get hashCode =>
    (myNumber == null ? 0 : myNumber.hashCode) +
    (myString == null ? 0 : myString.hashCode) +
    (myBoolean == null ? 0 : myBoolean.hashCode);

  factory OuterComposite.fromJson(Map<String, dynamic> json) => _$OuterCompositeFromJson(json);

  Map<String, dynamic> toJson() => _$OuterCompositeToJson(this);

  @override
  String toString() {
    return toJson().toString();
  }

}

