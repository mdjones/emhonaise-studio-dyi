.PHONY: all clean

obs = fast_and_bulbous_vcf_bom.csv \
	tin_teardrop_vcf_build_and_bom.csv \
	moldy_repature_vco_bom.csv

all: $(obs)
	@echo "All done!"


fast_and_bulbous_vcf_bom.csv: FAST+AND+BULBOUS+VCF+Build+and+BOM.pdf
	./nlc_bom_parser.py FAST+AND+BULBOUS+VCF+Build+and+BOM.pdf $@

tin_teardrop_vcf_build_and_bom.csv: TIN+TEARDROP+VCF+Build+and+BOM.pdf
	./nlc_bom_parser.py TIN+TEARDROP+VCF+Build+and+BOM.pdf $@

moldy_repature_vco_bom.csv: Moldy+Rapture+VCO+Build+and+BOM.pdf
	./nlc_bom_parser.py Moldy+Rapture+VCO+Build+and+BOM.pdf $@

TIN+TEARDROP+VCF+Build+and+BOM.pdf:
	curl https://static1.squarespace.com/static/5e6e99e8bd2f8a6de8454feb/t/67b2c8fc4cd7762cdddb9e5f/1739770119933/TIN+TEARDROP+VCF+Build+and+BOM.pdf -o $@

Moldy+Rapture+VCO+Build+and+BOM.pdf:
	curl https://static1.squarespace.com/static/5e6e99e8bd2f8a6de8454feb/t/673ed08878cdde46c7360794/1732169871081/Moldy+Rapture+VCO+Build+and+BOM.pdf -o $@

clean:
	rm -f $(obs)
